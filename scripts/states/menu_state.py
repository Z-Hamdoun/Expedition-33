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
        
        # Setup du background
        self.game = game
        self.bg_img = game.assets.backgrounds['menu']['main']
        if self.bg_img:
            self.bg_img = pygame.transform.scale(self.bg_img, (game.width, game.height))
        self.sound = SoundManager()

        # Setup poolice
        self.font = pygame.font.Font(None, 60)
        
        # Creation boutons
        # On les mets dans une liste ou dict
        cw, ch = game.width // 2, game.height // 2
        
        self.btn_play = Button(cw//2,7*ch//4 , "COMMENCER", self.font,(240,230,140), (255,215,0))
        self.btn_options = Button(cw,7*ch//4 , "SKINS", self.font,(240,230,140), (255,215,0))
        self.btn_quit = Button(3*cw//2,7*ch//4, "QUITTER", self.font,(240,230,140), (255,215,0))

        #Musique
        self.sound.play_music("accueil")
 
    def update(self):
        # Gere hover sur un boutton
        mouse_pos = pygame.mouse.get_pos()
        self.btn_play.update(mouse_pos)
        self.btn_options.update(mouse_pos)
        self.btn_quit.update(mouse_pos)
 
    def draw(self, surface):
        # Dessiner background
        if self.bg_img:
            surface.blit(self.bg_img, (0,0))
        else:
            surface.fill("gray")
            
        # Dessiner Buttons
        self.btn_play.draw(surface)
        self.btn_options.draw(surface)
        self.btn_quit.draw(surface)
 
    def handle_input(self, events):
        """Gere les entrees
        """
        for event in events:
            # Logique du Play Button
            if self.btn_play.is_clicked(event):
                # Entrer dans l'etat Play
                new_state = ThemeState(self.game)
                self.game.current_state = new_state
                self.sound.play_sound('bouton_confirm')
                
            # Logique boutton quitter
            if self.btn_quit.is_clicked(event):
                self.game.running = False
                
            # Logique boutton skins
            if self.btn_options.is_clicked(event):
                new_state = SkinState(self.game)
                self.game.current_state = new_state
                self.sound.play_sound('bouton_confirm')
  
