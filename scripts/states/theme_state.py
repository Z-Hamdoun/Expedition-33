import pygame
import os
from scripts.states.state import State
from scripts.states.play_state import PlayState
from scripts.ui import Button, ImgButton

class ThemeState(State):
    def __init__(self,game):
        super().__init__(game)

        self.game = game
        self.bg_img = game.assets.backgrounds['menu']['theme']
        # if self.bg_img:
        #     self.bg_img = pygame.transform.scale(self.bg_img, (game.width, game.height))
        
        self.font = pygame.font.Font(None,60)
        self.largeur = self.game.width
        self.hauteur = self.game.height
        self.choix_l = 250
        self.choix_h = 300
        self.choix = {}
        self.boutons = {}
        themes = ["forest","desert","snow"]
        for theme in themes:
            image = self.game.assets.backgrounds['game'][theme]
            cadre = pygame.transform.scale(image, (self.choix_l, self.choix_h))
            self.choix[theme] = cadre
        
        
        # Bouttons images
        self.theme_1 = ImgButton(image_surface=self.choix["snow"], x = self.largeur//4,y = 5*self.hauteur//8,color_base=(255, 215, 0), color_hover=(255, 255, 255))
        self.theme_2 = ImgButton(image_surface=self.choix["forest"], x = self.largeur//2,y = 5*self.hauteur//8,color_base=(255, 215, 0), color_hover=(255, 255, 255))
        self.theme_3 = ImgButton(image_surface=self.choix["desert"], x = 3*self.largeur//4,y = 5*self.hauteur//8,color_base=(255, 215, 0), color_hover=(255, 255, 255))    

    def text(self,texte,font,couleur,x,y,fenetre):
        txt_to_img = font.render(texte,True,couleur)
        rect = txt_to_img.get_rect()
        rect.center  = (x,y)
        fenetre.blit(txt_to_img,rect)
    
    
    def update(self):
        # Gere hover sur un boutton
        mouse_pos = pygame.mouse.get_pos()
        self.theme_1.update(mouse_pos)
        self.theme_2.update(mouse_pos)
        self.theme_3.update(mouse_pos)

    def draw(self,screen):
        if self.bg_img:
            screen.blit(self.bg_img, (0,0))
        else:
            screen.fill("gray")
        self.text("Selectionnez un thème",self.font,(240,230,140),self.largeur//2,self.hauteur//4,screen)
        self.theme_1.draw(screen)
        self.theme_2.draw(screen)
        self.theme_3.draw(screen)


    def handle_input(self, events):
        for event in events:
            if self.theme_1.is_clicked(event):
                theme = "snow"
                self.game.settings.game_ground_y = 620
                new_state = PlayState(self.game, theme)
                self.game.current_state = new_state
            if self.theme_2.is_clicked(event):
                theme = "forest"
                self.game.settings.game_ground_y = 650
                new_state = PlayState(self.game, theme)
                self.game.current_state = new_state
            if self.theme_3.is_clicked(event):
                theme = "desert"
                self.game.settings.game_ground_y = 575
                new_state = PlayState(self.game, theme)
                self.game.current_state = new_state
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from scripts.states.menu_state import MenuState
                    new_state = MenuState(self.game)
                    self.game.current_state = new_state
