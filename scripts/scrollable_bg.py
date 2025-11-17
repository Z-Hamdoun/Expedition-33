import pygame as py
from pygame.locals import *


py.init()

class background():
    def __init__(self,largeur = py.display.Info().current_w,hauteur = py.display.Info().current_h,img = 'bg.png', vitesse = 3):
        self.largeur = largeur
        self.hauteur = hauteur
        self.vitesse = 3
        self.img = py.image.load(img).convert()
        self.defilement_horizontal = 0
        self.pavage = ( self.largeur // self.img.get_width() ) + 1

    def maj(self):
        self.defilement_horizontal -= self.vitesse
        if abs(self.defilement_horizontal) > self.img.get_width():
            self.defilement_horizontal = 0
    
    def affiche(self,fenetre):
        for i in range(self.pavage):
            abscisse = self.img.get_width()*i + self.defilement_horizontal
            fenetre.blit(self.img, (abscisse,0))

    


