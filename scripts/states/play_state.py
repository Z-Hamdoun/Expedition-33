import pygame
from scripts.states.state import State
from scripts.player import Player
from scripts.scrollable_bg import background
from scripts.obstacles import ObstacleManager
from scripts.states.gameover_state import GameOverState

class PlayState(State):
    def __init__(self, game):
        super().__init__(game)
        # Initialize Entities
        self.game = game
        self.player = Player(game.settings, game.assets)
        self.bg = background(img=game.assets.backgrounds['background'])
        self.bg.vitesse = game.settings.game_game_speed
        
        # New Manager for Enemies (Supports Bosses/Waves)
        self.obstacle_manager = ObstacleManager(game.assets, game.settings)
        
        # Pause
        self.pause = False
        self.lost = False
        
        # Music
        # A completer
    
    def enter_state(self):
        # Code pour gerer la musique
        pass
    
    def update(self):
        if not self.pause:
            # Gestion du background
            self.bg.maj()

            # Entree joueur + physique
            keys = pygame.key.get_pressed()
            self.player.update(keys)

            # Ennemis
            self.obstacle_manager.update()

            # 4. Collision 
            collisions = pygame.sprite.spritecollide(self.player, self.obstacle_manager.obstacles, False)
            if collisions:
                # Entrer dans etat game_over
                self.game
                etat_menu = 'perdu'
    
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause = True
    
    def draw(self, surface):
        self.bg.affiche(surface)
        self.player.blit_me(surface)
        self.obstacle_manager.draw(surface)
        
    
    def desc(self):
        return 'play'