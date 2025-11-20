import pygame as pygame
from pygame.locals import *
import math

pygame.init()

class background():
    def __init__(self,settings,img = None , vitesse = 3):
        self.img = img
        self.settings = settings
        self.vitesse = 3
        self.img = pygame.transform.scale(self.img, (self.settings.game_width, self.settings.game_height))
        self.defilement_horizontal = 0
        self.pavage = math.ceil( self.settings.game_width / self.img.get_width() ) + 1

    def maj(self):
        self.defilement_horizontal -= self.settings.game_game_speed
        if abs(self.defilement_horizontal) > self.img.get_width():
            self.defilement_horizontal = 0
    
    def affiche(self,fenetre):
        for i in range(self.pavage):
            abscisse = self.img.get_width()*i + self.defilement_horizontal
            fenetre.blit(self.img, (abscisse,0))

    


