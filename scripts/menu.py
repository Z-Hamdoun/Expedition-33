import pygame 
from pygame.locals import *

pygame.font.init()



class Menu():
    def __init__(self,largeur = pygame.display.Info().current_w,hauteur = pygame.display.Info().current_h):
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = (255,255,255)
        self.police = pygame.font.Font(None,60)

    def text(self,texte,font,couleur,x,y,fenetre):
        txt_to_img = font.render(texte,True,couleur)
        rect = txt_to_img.get_rect()
        rect.center  = (x,y)
        fenetre.blit(txt_to_img,rect)

    def affichage(self,fenetre):
        fenetre.fill(self.couleur)
        self.text("Press ENTER to start",self.police,(0,0,0), self.largeur //2, self.hauteur //2,fenetre)
