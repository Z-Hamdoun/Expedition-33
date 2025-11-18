import pygame
import os

class AssetManager:
    """Classe permettant de gerer tout les assets pour une meilleur performance et lisibilite du code
    """
    def __init__(self):
        # Dossier principal du projet
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        # Dossier assets
        self.asset_dir = os.path.join(self.base_dir, 'assets')
        
        # Stockage des images dans des dictionnaires
        self.player_imgs = {}   # Will store {'run': [img1, img2], 'jump': img}
        self.backgrounds = {}
        self.enemies = {}
        # self.sounds = {}
        
        

   