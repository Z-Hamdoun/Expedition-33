import pygame
from scripts.states.state import State
from scripts.player import Player
from scripts.scrollable_bg import background
from scripts.obstacles import ObstacleManager

class PlayState(State):
    def __init__(self, game):
        super().__init__(game)
        # Initialize Entities
        self.player = Player(game.settings, game.assets)
        self.bg = background(img=game.assets.backgrounds['background'])
        
        # New Manager for Enemies (Supports Bosses/Waves)
        self.enemy_manager = ObstacleManager(game.assets, game.settings)
        
        # Music
        # A completer
    
    def enter_state(self):
        # Code pour gerer la musique
        pass
    
    def update(self):
        # Gestion du background
        self.bg.maj()
        
        # Entree joueur + physique
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        
        # Ennemis
        self.enemy_manager.update()
        
        # 4. Collision 
        if pygame.sprite.spritecollide(self.player, self.enemy_manager.obstacles, False):
            # Passer a l'etat game_over
            from states.game_over import GameOverState
            new_state = GameOverState(self.game, score=self.enemy_manager.score)
            new_state.enter_state()
            self.game.current_state = new_state