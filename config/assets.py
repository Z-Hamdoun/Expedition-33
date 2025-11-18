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
        self.sounds = {}
        
        
    
    def load_image(self,
        folder_path: str,
        filename: str,
        transparent: bool = True):
        """Permet de charger une image a partir d'un path

        Args:
            folder_path (str): path au dossier assets.
            filename (str): nom du fichier a charger.
            transparent (bool, optional): True pour les sprites, False pour le fond d'ecran. Defaults to True.

        Returns:
            _type_: _description_
        """
        # chemin complet
        path = os.path.join(self.asset_dir, *folder_path, filename)
        
        try:
            img = pygame.image.load(path)
            if transparent:
                return img.convert_alpha() # Pour les sprites (transparence)
            else:
                return img.convert()       # Pour les backgrounds (plus rapide)
        except FileNotFoundError:
            print(f"[AssetManager][Erreur]: Image introuvable a: {path}")
            # Placeholder pour montrer que le fichier manque, et ne pas arreter le jeu
            surf = pygame.Surface((50, 50))
            surf.fill((255, 0, 255)) 
            return surf

   