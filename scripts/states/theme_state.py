import pygame
import os
from scripts.states.state import State
from scripts.states.play_state import PlayState
from scripts.ui import Button, ImgButton

class ThemeState(State):
    def __init__(self,game):
        super().__init__(game)

        self.game = game
        self.bg_img = game.assets.backgrounds.get("background")
        if self.bg_img:
            self.bg_img = pygame.transform.scale(self.bg_img, (game.width, game.height))
        
        self.font = pygame.font.Font(None,60)
        self.largeur = self.game.width
        self.hauteur = self.game.height
        self.choix_l = 200
        self.choix_h = 400
        self.choix = {}
        self.boutons = {}
        self.theme_actuel = "foret"
        themes = ["foret","desert","ocean"]
        for theme in themes:
            cadre = pygame.surface.Surface((self.choix_l,self.choix_h))
            if theme == "ocean" : cadre.fill((0,100,255))
            if theme == "desert" : cadre.fill((240,200,100))
            if theme == "foret" : cadre.fill((34,139,34))
            self.choix[theme] = cadre
        
        
        # Bouttons images
        image_surface = self.choix['ocean']
        self.theme_1 = ImgButton(image_surface=image_surface,
            x = self.largeur//4,y = 5*self.hauteur//8,color_base=(255, 215, 0), color_hover=(255, 255, 255))

    
    def text(self,texte,font,couleur,x,y,fenetre):
        txt_to_img = font.render(texte,True,couleur)
        rect = txt_to_img.get_rect()
        rect.center  = (x,y)
        fenetre.blit(txt_to_img,rect)
    
    
    def update(self):
        # Gere hover sur un boutton
        mouse_pos = pygame.mouse.get_pos()
        self.theme_1.update(mouse_pos)

    def draw(self,screen):
        if self.bg_img:
            screen.blit(self.bg_img, (0,0))
        else:
            screen.fill("gray")
        self.text("Selectionnez un thème",self.font,(0,0,0),self.largeur//2,self.hauteur//4,screen)
        self.theme_1.draw(screen)
        self.text("Ocean", self.font,(0,0,0),self.largeur//4,self.hauteur//4  + self.choix_h//2 + 100,screen)

        #is_selected = (theme_actuel == "desert")
        #self.boutons["desert"] = self.img_button(self.choix["desert"],self.largeur//2,5*self.hauteur//8, fenetre, is_selected)
        #self.text("Desert", self.police,(0,0,0),self.largeur//2,self.hauteur//4  + self.choix_h//2  + 100, fenetre)
        #
        #is_selected = (theme_actuel == "foret")
        #self.boutons["foret"] = self.img_button(self.choix["foret"],3*self.largeur//4,5*self.hauteur//8, fenetre, is_selected)
        #self.text("Foret", self.police,(0,0,0),3*self.largeur//4,self.hauteur//4  + self.choix_h//2  + 100, fenetre)


    def handle_input(self, events):
        for event in events:
            if self.theme_1.is_clicked(event):
                # Entrer dans l'etat Play
                new_state = ThemeState(self.game)
                self.game.current_state = new_state
                