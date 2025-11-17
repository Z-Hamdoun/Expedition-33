import pygame
from pygame.locals import *
from dimension import dimension
from random import randint
import os

HEIGHT = dimension()['HEIGHT']
WIDTH  = dimension()['WIDTH']

class Obstacle(pygame.sprite.Sprite):
    """ Classe générale dont vont hériter les différents obstacles"""
    def __init__(self,image,type):
        self.image = image
        self.type = type
        super().__init__()
        self.rect = self.image[self.type].get_rect() 
        self.rect.x = WIDTH
    
    def update(self,obstacles):
        self.rect.x -= 0 #Remplacer par le nom de la vitesse de jeu
        if self.rect.x < -self.rect.width:
            obstacles.pop()

class Oiseau(Obstacle):
    """Se baisser ou utiliser jet-pack pour l'éviter"""
    def __init__(self,image):
        self.type = 0
        super().__init__(image,self.type)
        self.rect.y = HEIGHT - 20

class LargeCactus(Obstacle):
    """Sauter par dessus"""
    def __init__(self,image):
        self.type = randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 0 #à préciser

class SmallCactus(Obstacle):
    """Sauter par dessus"""
    def __init__(self,image):
        self.type = randint(0,2)
        super().__init__(image,self.type)
        self.rect.y = 0 #à préciser

class Pics(SmallCactus):
    """Mettre un coup de griffe pour les passer"""
    def __init__(self,image):
        self.type = 0
        super().__init__(image)
        