import pygame
import os
from scripts.states.state import State
from scripts.states.play_state import PlayState
from scripts.states.theme_state import ThemeState
from scripts.ui import Button
from scripts.states.skins_state import SkinState
from scripts.sound_management import SoundManager

class MenuState(State):
    def __init__(self, game):
        super().__init__(game)
        # Initialisation de l'arrière plan
        self.game = game
        self.bg_img = game.assets.backgrounds['menu']['main']
        if self.bg_img:
            self.bg_img = pygame.transform.scale(self.bg_img, (game.width, game.height))
        # Initialisation du son
        self.sound = SoundManager()
        # Définition de la police
        self.font = pygame.font.Font(None, 30)
        # Creation des boutons
        cw, ch = game.width // 2, game.height // 2
        self.btn_play = Button(cw//2,7*ch//4 , "COMMENCER", self.font,(240,230,140), (255,215,0))
        self.btn_skins = Button(cw,7*ch//4 , "SKINS", self.font,(240,230,140), (255,215,0))
        self.btn_quit = Button(3*cw//2,7*ch//4, "QUITTER", self.font,(240,230,140), (255,215,0))
        
        
        #Musique
        self.sound.play_music("accueil")

    def text(self,texte,font,couleur,x,y,fenetre):
        txt_to_img = font.render(texte,True,couleur)
        rect = txt_to_img.get_rect()
        rect.center  = (x,y)
        fenetre.blit(txt_to_img,rect)

    
    def update(self):
        # Vérifie si un des boutons a été survolé
        mouse_pos = pygame.mouse.get_pos()
        self.btn_play.update(mouse_pos)
        self.btn_skins.update(mouse_pos)
        self.btn_quit.update(mouse_pos)
 

    def draw(self, surface):
        # Dessine l'arrière plan
        if self.bg_img:
            surface.blit(self.bg_img, (0,0))
        else:
            surface.fill("gray")  
        # Dessine les boutons et meilleur score
        self.btn_play.draw(surface)
        self.btn_skins.draw(surface)
        self.btn_quit.draw(surface)
        self.text("High score = " + str(self.game.settings.game_high_score),self.font,(0,0,0),self.game.width - 150,20,surface)
 

    def handle_input(self, events):
        # Collecte des évènements
        for event in events:
            # Logique du bouton play
            if self.btn_play.is_clicked(event):
                new_state = ThemeState(self.game)
                self.game.current_state = new_state
                
            # Logique du boutton quitter
            if self.btn_quit.is_clicked(event):
                self.game.running = False
                
            # Logique du bouton skins
            if self.btn_skins.is_clicked(event):
                new_state = SkinState(self.game)
                self.game.current_state = new_state
  
