import pygame
import os
from scripts.states.state import State
from scripts.ui import ImgButton
 
class SkinState(State):
    def __init__(self, game):
        super().__init__(game)
        
        # Setup du background
        self.game = game
        self.bg_img = game.assets.backgrounds['menu']['skins']
        if self.bg_img:
            self.bg_img = pygame.transform.scale(self.bg_img, (game.width, game.height))
            
        # Setup poolice
        self.font = pygame.font.Font(None, 60)
        
        # Creation boutons
        # On les mets dans une liste ou dict
        cw, ch = self.game.width // 2, self.game.height // 2
        self.choix = {}
        self.choix_l = 200
        self.choix_h = 400
        skins = ["forest","snow","desert"]
        for skin in skins:
            image = self.game.assets.backgrounds['game'][skin]
            cadre = pygame.transform.scale(image, (self.choix_l, self.choix_h))
            self.choix[skin] = cadre
        
        self.img1 = ImgButton(self.game.width//4, 5*self.game.height//8, (0,0,0), (255,215,0),self.choix["snow"])
        self.img2 = ImgButton(self.game.width//2, 5*self.game.height//8, (0,0,0), (255,215,0),self.choix["forest"])
        self.img3 = ImgButton(3*self.game.width//4, 5*self.game.height//8, (0,0,0), (255,215,0),self.choix["desert"])
 
    def update(self):
        # Gere hover sur un boutton
        mouse_pos = pygame.mouse.get_pos()
        self.img1.update(mouse_pos)
        self.img2.update(mouse_pos)
        self.img3.update(mouse_pos)

 
    def draw(self, surface):
        # Dessiner background
        if self.bg_img:
            surface.blit(self.bg_img, (0,0))
        else:
            surface.fill("gray")
            
        # Dessiner Buttons
        self.img1.draw(surface)
        self.img2.draw(surface)
        self.img3.draw(surface)
        self.img1.outline(surface,self.img1.is_selected)
        self.img2.outline(surface,self.img2.is_selected)
        self.img3.outline(surface,self.img3.is_selected)
 
    def handle_input(self, events):
        """Gere les entrees
        """
        for event in events:
            if self.img1.is_clicked(event):
                self.img1.is_selected = True
                self.img2.is_selected = False
                self.img3.is_selected = False

                
 
            if self.img2.is_clicked(event):
                self.img1.is_selected = False
                self.img2.is_selected = True
                self.img3.is_selected = False
                

            if self.img3.is_clicked(event):
                self.img1.is_selected = False
                self.img2.is_selected = False
                self.img3.is_selected = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from scripts.states.menu_state import MenuState
                    new_state = MenuState(self.game)
                    self.game.current_state = new_state
