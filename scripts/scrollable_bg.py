import pygame as pygame
from pygame.locals import *
import math

pygame.init()

class background():
    def __init__(self,settings,img = None):
        self.img = img
        self.settings = settings
        self.img = pygame.transform.scale(self.img, (self.settings.game_width, self.settings.game_height)).convert()
        self.width = self.img.get_width()
        self.defilement_horizontal = 0
        self.pavage = math.ceil(self.settings.game_width / self.width) + 1

    def maj(self):
        self.defilement_horizontal -= self.settings.game_game_speed
        if self.defilement_horizontal <= -self.width:
            self.defilement_horizontal += self.width
    
    def affiche(self,fenetre):
        for i in range(self.pavage):
            x_position = (self.width * i) + self.defilement_horizontal
            fenetre.blit(self.img, (int(x_position), 0))

    


