import pygame
from scripts.states.state import State
from scripts.player import Player
from scripts.scrollable_bg import background
from scripts.obstacles import ObstacleManager
from scripts.states.gameover_state import GameOverState
from scripts.states.pause_state import PauseState
from scripts.difficulté import GestionDifficulte

class PlayState(State):
    def __init__(self, game, theme):
        super().__init__(game)
        # Initialize Entities
        self.game = game
        self.difficulté = GestionDifficulte()
        self.difficulté.reset_depart()
        self.player = Player(game.settings, game.assets)
        self.bg = background(img=game.assets.backgrounds['game'][theme])
        self.bg.vitesse = self.difficulté.update()[0]
        
        # New Manager for Enemies (Supports Bosses/Waves)
        self.obstacle_manager = ObstacleManager(game.assets, game.settings)
        
        # Score
        self.score = 0
        self.score_font = pygame.font.Font(None, 60)
        
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
            self.bg.vitesse = self.difficulté.update()[0]
            self.game.settings.game_game_speed = self.bg.vitesse

            # Entree joueur + physique
            keys = pygame.key.get_pressed()
            self.player.update(keys)

            # Ennemis
            self.obstacle_manager.update()
            
            self.score += int(self.game.settings.game_game_speed / 10)

            # 4. Collision 
            collisions = pygame.sprite.spritecollide(self.player, self.obstacle_manager.obstacles, False)
            if collisions:
                # Entrer dans etat game_over
                self.game.current_state = GameOverState(self.game, final_score=self.score, prev_state=self)
    
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.current_state = PauseState(self.game, prev_state=self)
    
    def draw(self, surface):
        self.bg.affiche(surface)
        self.player.blit_me(surface)
        self.obstacle_manager.draw(surface)
        
        score_text = self.score_font.render(f'Score: {self.score}', True, (0, 0, 0))
        surface.blit(score_text, (self.game.width - 250, 20))
        
    
    def desc(self):
        return 'play'