import pygame
from pygame.locals import *
from random import randint
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


dico_images = { 'Oiseau' : [pygame.image.load(os.path.join("assets","Bird", "Bird1.png"))],
                'LargeCactus' : [pygame.image.load(os.path.join("assets","Cactus","LargeCactus1.png")),pygame.image.load(os.path.join("assets", "Cactus","LargeCactus2.png")),pygame.image.load(os.path.join("assets", "Cactus","LargeCactus3.png"))],
                'SmallCactus' : [pygame.image.load(os.path.join("assets","Cactus","SmallCactus1.png")),pygame.image.load(os.path.join("assets", "Cactus","SmallCactus2.png")),pygame.image.load(os.path.join("assets", "Cactus","SmallCactus3.png"))]}

sol = 500
WIDTH  = 1200

class Obstacle(pygame.sprite.Sprite):
    """ Classe générale dont vont hériter les différents obstacles"""
    def __init__(self,image,type):
        self.image = image
        self.type = type
        super().__init__()
        self.rect = self.image[self.type].get_rect() 
        self.rect.x = WIDTH
    
    def update(self,obstacles,game_speed):
        self.rect.x -= game_speed 
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    
    def draw(self, ecran):
        ecran.blit(self.image[self.type], self.rect)

class Oiseau(Obstacle):
    """Se baisser ou utiliser jet-pack pour l'éviter"""
    def __init__(self):
        self.type = 0
        self.image = dico_images['Oiseau']
        super().__init__(self.image,self.type)
        aleatoire = randint(-5,15) #l'oiseau peut apparaître plus ou moins haut
        self.rect.y = sol - 70 + aleatoire

class LargeCactus(Obstacle):
    """Sauter par dessus"""
    def __init__(self):
        self.type = randint(0,2)
        self.image = dico_images['LargeCactus']
        super().__init__(self.image,self.type)
        self.rect.y = sol #à préciser

class SmallCactus(Obstacle):
    """Sauter par dessus"""
    def __init__(self):
        self.type = randint(0,2)
        self.image = dico_images["SmallCactus"]
        super().__init__(self.image,self.type)
        self.rect.y = sol + 30 #à préciser

class Pics(SmallCactus):
    """Mettre un coup de griffe pour les passer"""
    def __init__(self):
        self.type = 0
        super().__init__()
        