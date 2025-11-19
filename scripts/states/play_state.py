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