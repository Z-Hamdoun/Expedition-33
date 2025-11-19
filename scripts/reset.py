import os
from scripts.player import *
from scripts.scrollable_bg import *

def reinitialiser(settings):
    obstacles = []
    player = Player(settings)
    default_bg_path = os.path.join("assets", "Backgrounds", "Game","tall_trees.png")
    bg = background(img=default_bg_path)
    return player, obstacles, bg, 0