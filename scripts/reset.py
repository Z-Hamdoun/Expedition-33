import os
from scripts.player import *
from scripts.scrollable_bg import *

def reinitialiser():
    obstacles = []
    player = Player()
    default_bg_path = os.path.join("assets", "Backgrounds", "Game","tall_trees.png")
    bg = background(img=default_bg_path)
    return player, obstacles, bg