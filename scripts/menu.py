import pygame 
from pygame.locals import *
import os

pygame.font.init()



class Menu():
    def __init__(self,largeur = pygame.display.Info().current_w,hauteur = pygame.display.Info().current_h,img = None):
        self.largeur = largeur
        self.hauteur = hauteur
        self.police = pygame.font.Font(None,60)
        self.bg = pygame.image.load(img).convert()
        self.bg = pygame.transform.scale(self.bg, (self.largeur, self.hauteur))

    def button(self,texte,font,couleur1,couleur2,x,y,fenetre):
        couleur = couleur1
        souris = pygame.mouse.get_pos()
        txt_to_img = font.render(texte,True,couleur1)
        rect = txt_to_img.get_rect()
        rect.center  = (x,y)
        if rect.collidepoint(souris): couleur = couleur2
        else : couleur = couleur1
        bouton = font.render(texte,True,couleur)
        fenetre.blit(bouton,rect)
        return rect

    def background(self,fenetre):
        fenetre.blit(self.bg, (0, 0))

class MainMenu(Menu):
    def __init__(self,largeur,hauteur,img):
        super().__init__(largeur, hauteur, img)

    def affichage(self,fenetre):
        self.background(fenetre)
        bonton_start = self.button("NOUVELLE PARTIE", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2  -50, fenetre)
        bouton_options = self.button("OPTIONS", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2 + 50, fenetre)
        bouton_quitter = self.button("QUITTER", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2 + 150, fenetre)
        return {"start":bonton_start,"options":bouton_options,"quitter":bouton_quitter}