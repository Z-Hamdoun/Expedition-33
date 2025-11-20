import pygame
from scripts.states.state import State
from scripts.player import Player
from scripts.scrollable_bg import background
from scripts.obstacles import ObstacleManager
from scripts.states.gameover_state import GameOverState
from scripts.states.pause_state import PauseState
from scripts.bullet import Bullet
from scripts.difficulté import GestionDifficulte

class PlayState(State):
    def __init__(self, game, theme):
        super().__init__(game)
        # Initialisation
        self.game = game
        self.difficulté = GestionDifficulte()
        self.difficulté.reset_depart()
        self.player = Player(game.settings, game.assets)
        self.bg = background(img=game.assets.backgrounds['game'][theme])
        self.bg.vitesse = self.difficulté.update()[0]
        
        # Gestionnaire des obstacles
        self.obstacle_manager = ObstacleManager(game.assets, game.settings)
        
        # Groupe qui contient les balles
        self.bullets = pygame.sprite.Group()
        
        # Score
        self.score = 0
        self.score_font = pygame.font.Font(None, 60)
        
        
        # Musique
        # A completer
    
    def enter_state(self):
        # Code pour gerer la musique
        pass
    
    def update(self):
        # Gestion du background
        self.bg.maj()
        self.bg.vitesse = self.difficulté.update()[0]
        self.game.settings.game_game_speed = self.bg.vitesse

        # Entree joueur + physique
        keys = pygame.key.get_pressed()
        self.player.update(keys)

        # Ennemis
        self.obstacle_manager.update()
        
        # Balles
        self.bullets.update()
            
        self.score += int(self.game.settings.game_game_speed / 10)
        
        hits = pygame.sprite.groupcollide(self.bullets, self.obstacle_manager.obstacles, True, True)  
        if hits:
            pass

        # 4. Collision 
        collisions = pygame.sprite.spritecollide(self.player, self.obstacle_manager.obstacles, False)
        powerups = pygame.sprite.spritecollide(self.player, self.obstacle_manager.powerups, True) # True pour supprimer le pistolet
        if collisions:
            if not self.game.settings.debug_mode:
                # Entrer dans etat game_over
                self.game.current_state = GameOverState(self.game, final_score=self.score, prev_state=self)
            else:
                pygame.time.delay(200)
        if powerups:
            self.player.equip_gun()
            # SON RECUPERER GUN
            
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.current_state = PauseState(self.game, prev_state=self)
                # Debogage
                if event.key == pygame.K_h:
                    self.game.settings.debug_mode = not self.game.settings.debug_mode
                if event.key == pygame.K_PAGEUP:
                    self.game.settings.game_game_speed += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.player.end_jump()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Click gauche
                    if self.player._can_shoot():
                        self.shoot(event.pos)
                        self.player._shoot()
                    else:
                        print("Pas de munitions")
    
    def shoot(self, mouse_pos):
        """Tire vers la position de la souris"""
        start_pos = self.player.rect.center
        
        # Creer la balle
        new_bullet = Bullet(start_pos, mouse_pos, self.game.assets)
        
        # Ajouter au groupe
        self.bullets.add(new_bullet)
    
    def _draw_ammo_ui(self, surface):
        """Represente les balles disponibles"""
        padding = 10
        radius = 10
        start_x = 20
        y_pos = 80
        
        bullet_img = self.game.assets.other.get('bullet')
        
        for i in range(self.player.max_ammo):
            # Calculer la position de chaque balle
            x_pos = start_x + (i * (radius * 2 + padding))
            
            if i < self.player.current_ammo:
                surface.blit(bullet_img, (x_pos, y_pos))
                
            
    
    def draw(self, surface):
        self.bg.affiche(surface)
        self.player.blit_me(surface)
        self.obstacle_manager.draw(surface)
        
        self.bullets.draw(surface)
        self._draw_ammo_ui(surface)
        
        score_text = self.score_font.render(f'Score: {self.score}', True, (0, 0, 0))
        surface.blit(score_text, (self.game.width - 250, 20))
        
        if self.game.settings.debug_mode:
            # Hitbox du joueur en rouge
            pygame.draw.rect(surface, (255, 0, 0), self.player.rect, 2)
            
            # Hitbox des obstacles en bleu
            for obs in self.obstacle_manager.obstacles:
                pygame.draw.rect(surface, (0, 0, 255), obs.rect, 2)
                
            # Balles en Jaune
            for bullet in self.bullets:
                pygame.draw.rect(surface, (255, 255, 0), bullet.rect, 2)
        
    
    def desc(self):
        return 'play'