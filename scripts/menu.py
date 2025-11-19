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

    def img_button(self, image_surface, x, y, fenetre, selected=False):
        souris = pygame.mouse.get_pos()
        rect = image_surface.get_rect()
        rect.center = (x, y)
        fenetre.blit(image_surface, rect)
        if rect.collidepoint(souris):
            pygame.draw.rect(fenetre, (255, 255, 255), rect, 3)
        if selected:
            pygame.draw.rect(fenetre, (255, 215, 0), rect, 6)
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
    
class OptionMenu(Menu):
    def __init__(self,largeur,hauteur,img):
        super().__init__(largeur, hauteur, img)

    def affichage(self,fenetre,mode):
        boutons = {}
        self.background(fenetre)
        self.text("OPTIONS",self.police,(0,0,0),self.largeur//2,self.hauteur//4,fenetre)
        boutons["themes"] = self.button("Thème", self.police, (0,0,0),(0,0,0), 3*self.largeur // 4, self.hauteur // 2 , fenetre)
        boutons["difficulté"] = self.button("Difficulté", self.police, (0,0,0),(0,0,0), self.largeur // 4, self.hauteur // 2  , fenetre)
        modes = ["Facile","Moyen","Difficile"]
        for i,diff in enumerate(modes):
            if diff.lower() == mode.lower() : color = (255,215,0) 
            else : color = (0,0,0)
            boutons[diff] = self.button(diff,self.police,color,(255,215,0),self.largeur//4,self.hauteur//2  + (i+2)*50,fenetre) 
        return boutons


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
        self.overlay = pygame.Surface((self.hauteur//2,3*self.largeur//8))
        self.overlay.fill((255,255,255))
        self.overlay.set_alpha(180)
        self.overlay_rect = self.overlay.get_rect()
        self.overlay_rect.center = (self.largeur//2, self.hauteur//2)
        

    def affichage(self,fenetre):
        fenetre.blit(self.overlay,self.overlay_rect)
        self.text("PAUSE",self.police,(255,0,0),self.largeur//2,self.hauteur//4,fenetre)
        quitter_pause = self.button("Quitter", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2  + 200, fenetre)
        reprendre = self.button("Reprendre", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2 , fenetre)
        bouton_rejouer = self.button("Rejouer", self.police, (0,0,0),(255,215,0), self.largeur // 2, self.hauteur // 2  + 100, fenetre)
        return {"quitter_pause":quitter_pause,"reprendre":reprendre,"rejouer_pause":bouton_rejouer}

class ThemeMenu(Menu):
    def __init__(self,largeur,hauteur,img):
        super().__init__(largeur, hauteur, img)
        self.choix_l = 200
        self.choix_h = 400
        self.choix = {}
        themes = ["foret","desert","ocean"]
        for theme in themes:
            cadre = pygame.surface.Surface((self.choix_l,self.choix_h))
            if theme == "ocean" : cadre.fill((0,100,255))
            if theme == "desert" : cadre.fill((240,200,100))
            if theme == "foret" : cadre.fill((34,139,34))
            self.choix[theme] = cadre
    

    def affichage(self,fenetre,theme_actuel):
        self.background(fenetre)
        self.text("Selectionnez un thème",self.police,(0,0,0),self.largeur//2,self.hauteur//4,fenetre)
        boutons = {}
        is_selected = (theme_actuel == "ocean")
        boutons["theme_ocean"] = self.img_button(self.choix["ocean"],self.largeur//4,5*self.hauteur//8, fenetre, is_selected)
        self.text("Ocean", self.police,(0,0,0),self.largeur//4,self.hauteur//4  + self.choix_h//2 + 100,fenetre)

        is_selected = (theme_actuel == "desert")
        boutons["theme_desert"] = self.img_button(self.choix["desert"],self.largeur//2,5*self.hauteur//8, fenetre, is_selected)
        self.text("Desert", self.police,(0,0,0),self.largeur//2,self.hauteur//4  + self.choix_h//2  + 100, fenetre)

        # 3. Forest (Right)
        is_selected = (theme_actuel == "foret")
        boutons["theme_foret"] = self.img_button(self.choix["foret"],3*self.largeur//4,5*self.hauteur//8, fenetre, is_selected)
        self.text("Foret", self.police,(0,0,0),3*self.largeur//4,self.hauteur//4  + self.choix_h//2  + 100, fenetre)


        