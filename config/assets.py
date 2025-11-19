import pygame
import os

class AssetManager:
    """Classe permettant de gerer tout les assets pour une meilleur performance et lisibilite du code
    """
    def __init__(self):
        # Dossier principal du projet
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Dossier assets
        self.asset_dir = os.path.join(self.base_dir, 'assets')
        
        # Stockage des images dans des dictionnaires
        self.player_imgs = {}   # Format {'run': [img1, img2], 'jump': img}
        self.obstacles = {'statique': {'cactus': []}, 'dynamique': {'oiseau': []}} # format {'statique': {'cactus': {...}, 'arbre':{...}, ...}, 'dynamique': {'bird': ...}}
        self.backgrounds = {}
        self.enemies = {}
        self.sounds = {}
        
        self.other = {}
        
        # Charger tout les assets
        self.load_all()
    
    def load_image(self,
        folder_path: list[str],
        filename: str,
        transparent: bool = True):
        """Permet de charger une image a partir d'un path

        Args:
            folder_path (list): liste de sous dossiers.
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
    
    def load_all(self):
        print("[AssetManager][Info] Chargement des assets ...")
        
        # --- Player ---
        
        # A changer lors de l'ajout de skins
        self.player_imgs['run'] = [
            self.load_image(['Dino'], 'DinoRun1.png'),
            self.load_image(['Dino'], 'DinoRun2.png')
        ]
        self.player_imgs['jump'] = self.load_image(['Dino'], 'DinoJump.png')
        self.player_imgs['duck'] = [
            self.load_image(['Dino'], 'DinoDuck1.png'),
            self.load_image(['Dino'], 'DinoDuck2.png')
        ]

        # --- Backgrounds ---
        # transparent=False pour plus de performance
        self.backgrounds['background'] = self.load_image(['Backgrounds', 'Game'], 'tall_trees.png', transparent=False)
        
        # --- Obstacles ----
        # Statique
        # Cactus
        self.obstacles['statique']['cactus'] = []
        for i in range(6):
            self.obstacles['statique']['cactus'].append(
                self.load_image(['obstacles', 'statique', 'cactus'], f'{i}.png'))
        print(self.obstacles)

        # A completer
            
            
        # Dynamique
        self.obstacles['dynamique']['oiseau'] = [self.load_image(['obstacles', 'dynamique', 'oiseau'], f'1.png'),
            self.load_image(['obstacles', 'dynamique', 'oiseau'], f'2.png')]
        
        # --- Other ----
        self.other['bullet'] = self.load_image(['other'], 'bullet.png')
        
        # --- Sons ---
        
        # A completer
        
        print("[AssetManager][Success] Assets charges!")

   