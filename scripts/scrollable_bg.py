import pygame as pygame
from pygame.locals import *
import math

pygame.init()

class background():
    def __init__(self,largeur = pygame.display.Info().current_w,hauteur = pygame.display.Info().current_h,img = 'bg.png', vitesse = 3):
        self.largeur = largeur
        self.hauteur = hauteur
        self.vitesse = 3
        self.img = pygame.image.load(img).convert()
        self.img = pygame.transform.scale(self.img, (self.largeur, self.hauteur))
        self.defilement_horizontal = 0
        self.pavage = math.ceil( self.largeur / self.img.get_width() ) + 1

    def maj(self):
        self.defilement_horizontal -= self.vitesse
        if abs(self.defilement_horizontal) > self.img.get_width():
            self.defilement_horizontal = 0
    
    def affiche(self,fenetre):
        for i in range(self.pavage):
            abscisse = self.img.get_width()*i + self.defilement_horizontal
            fenetre.blit(self.img, (abscisse,0))

    


