# game.py
import pygame
from config.settings import Settings
from config.assets import AssetManager
from scripts.states.menu_state import MenuState

class Game:
    """Classe pour gerer le jeu
    """
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        
        self.settings = Settings()
        resolution = pygame.display.Info()
        self.width, self.height= resolution.current_w, resolution.current_h
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        # self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption(self.settings.game_title)
        self.clock = pygame.time.Clock()
        
        # Chargement des assets
        self.assets = AssetManager() 
        
        # Bool pour indiquer si le jeu est en cours
        self.running = True
        
        self.player = None
        # Menu
        self.current_state = MenuState(self)

    def run(self):
        while self.running:
            # Collecte des evenements
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    self.settings.save_settings()
            
            # Logique de l'etat actuel
            self.current_state.handle_input(events)
            self.current_state.update()
            
            # Dessiner 
            self.current_state.draw(self.screen)
            
            # Actualiser le jeu 
            pygame.display.update()
            self.clock.tick(self.settings.game_fps)

        # Sauvegarde des parametres et high_score
        self.settings.save_settings()
        pygame.quit()