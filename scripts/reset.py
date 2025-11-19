import os
from scripts.player import *
from scripts.scrollable_bg import *

def reinitialiser(settings,assets):
    obstacles = pygame.sprite.Group()
    player = Player(settings,assets)
    default_bg_path = os.path.join("assets", "Backgrounds", "Game","tall_trees.png")
    bg = background(img=assets.backgrounds['background'])
    return player, obstacles, bg,