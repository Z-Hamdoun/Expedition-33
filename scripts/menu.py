import pygame 
from pygame.locals import *


pygame.font.init()



class Menu():
    def __init__(self,largeur = pygame.display.Info().current_w,hauteur = pygame.display.Info().current_h,img = None):
        self.largeur = largeur
        self.hauteur = hauteur
        self.police = pygame.font.Font(None,60)
        if img is not None:
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


    def text(self,texte,font,couleur,x,y,fenetre):
        txt_to_img = font.render(texte,True,couleur)
        rect = txt_to_img.get_rect()
        rect.center  = (x,y)
        fenetre.blit(txt_to_img,rect)

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
    
class OptionMenu(Menu):
    def __init__(self,largeur,hauteur,img):
        super().__init__(largeur, hauteur, img)

    def affichage(self,fenetre):
        self.background(fenetre)
        self.text("OPTIONS",self.police,(0,0,0),self.largeur//2,self.hauteur//4,fenetre)
        bouton_themes = self.button("Thème", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2 , fenetre)
        bouton_difficulté = self.button("Difficulté", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2  + 100 , fenetre)
        return {"themes":bouton_themes,"difficulte":bouton_difficulté}


class GameOverMenu(Menu):
    def __init__(self,largeur,hauteur):
        super().__init__(largeur,hauteur,None)
        self.overlay = pygame.Surface((largeur,hauteur))
        self.overlay.fill((255,255,255))
        self.overlay.set_alpha(180)

    def affichage(self,fenetre,score):
        fenetre.blit(self.overlay,(0,0))
        self.text("GAME OVER",self.police,(255,0,0),self.largeur//2,self.hauteur//4,fenetre)
        self.text("Score final : " + str(score) ,self.police,(255,215,0),self.largeur//2,self.hauteur//2,fenetre)
        bouton_quitter = self.button("Quitter", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2  + 200, fenetre)
        bouton_rejouer = self.button("Rejouer", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2  + 100, fenetre)
        return {"quitter_over":bouton_quitter,"rejouer_over":bouton_rejouer}
    
class PauseMenu(Menu):
    def __init__(self,largeur,hauteur):
        super().__init__(largeur,hauteur,None)
        self.overlay = pygame.Surface((self.largeur,self.hauteur))
        self.overlay.fill((255,255,255))
        self.overlay.set_alpha(180)

    def affichage(self,fenetre):
        fenetre.blit(self.overlay,(0,0))
        self.text("PAUSE",self.police,(255,0,0),self.largeur//2,self.hauteur//4,fenetre)
        quitter_pause = self.button("Quitter", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2  + 200, fenetre)
        reprendre = self.button("Reprendre", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2 , fenetre)
        bouton_rejouer = self.button("Rejouer", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2  + 100, fenetre)
        return {"quitter_pause":quitter_pause,"reprendre":reprendre,"rejouer_pause":bouton_rejouer}
