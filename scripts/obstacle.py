import pygame
from pygame.locals import *
from dimension import dimension

HEIGHT = dimension()['HEIGHT']
WIDTH  = dimension()['WIDTH']

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Oiseau(Obstacle):
    """Se baisser ou utiliser jet-pack pour l'éviter"""
    def __init__(self):
        super().__init__()
        self.x = 50 #Taille horizontale
        self.y = 10 #Taille verticale

class Cactus(Obstacle):
    """Sauter par dessus"""
    def __init__(self):
        super().__init__()
        self.x = 50 #Taille horizontale
        self.y = 10 #Taille verticale

class Pics(Cactus):
    """Mettre un coup de griffe pour les passer"""
    def __init__(self):
        super().__init__()
        