# game.py
import pygame
from config.settings import Settings
from config.assets import AssetManager

class Game:
    """Class pour gerer le jeu
    """
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption(self.settings.game_title)
        self.clock = pygame.time.Clock()
        
        # Chargement des assets
        self.assets = AssetManager() 
        
        # Bool pour indiquer si le jeu est en cours
        self.running = True
        # Menu
        self.current_state = None

    def run(self):
        while self.running:
            # Collecte des evenements
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Logique de l'etat actuel
            self.current_state.handle_input(events)
            self.current_state.update()
            
            # Dessiner 
            self.current_state.draw(self.screen)
            
            # Actualiser le jeu 
            pygame.display.update()
            self.clock.tick(self.settings.game_fps)

        self.settings.save_settings()
        pygame.quit()