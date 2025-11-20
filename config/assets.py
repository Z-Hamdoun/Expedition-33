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
        self.skins = {}  
        self.obstacles = {'statique': {'cactus': []}, 'dynamique': {'oiseau': []}} # format {'statique': {'cactus': {...}, 'arbre':{...}, ...}, 'dynamique': {'bird': ...}}
        self.backgrounds = {'game': {}, 'menu': {}}
        self.enemies = {}
        self.sounds = {}
        
        self.other = {}
        
        # Charger tout les assets
        self.load_all()
    
    def load_image(self,
        folder_path: list[str],
        filename: str,
        transparent: bool = True,
        size=None):
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
                img = img.convert_alpha() # Pour les sprites (transparence)
            else:
                img = img.convert()       # Pour les backgrounds (plus rapide)
            
            if size is not None:
                img = pygame.transform.scale(img, size)
            return img
        except FileNotFoundError:
            print(f"[AssetManager][Erreur]: Image introuvable a: {path}")
            # Placeholder pour montrer que le fichier manque, et ne pas arreter le jeu
            surf = pygame.Surface((50, 50))
            surf.fill((255, 0, 255)) 
            return surf
    
    def load_all(self):
        print("[AssetManager][Info] Chargement des assets ...")
        
        # --- Player ---
        PLAYER_SIZE = (20, 20) 
        skins = ['forest', 'snow', 'desert']
        for skin in skins:
            self.skins[skin] = {}
            
            self.skins[skin]['run'] = [
                self.load_image(['skins', skin], 'DinoRun1.png', PLAYER_SIZE),
                self.load_image(['skins', skin], 'DinoRun2.png', PLAYER_SIZE)
            ]
            self.skins[skin]['jump'] = self.load_image(['skins', skin], 'DinoJump.png', PLAYER_SIZE)
            self.skins[skin]['duck'] = [
                self.load_image(['skins', skin], 'DinoDuck1.png', PLAYER_SIZE),
                self.load_image(['skins', skin], 'DinoDuck2.png', PLAYER_SIZE)
            ]

        # --- Backgrounds ---
        # transparent=False pour plus de performance
        
        # Game backgrounds
        self.backgrounds['game']['snow'] = self.load_image(['backgrounds', 'game'], 'snow.png', transparent=False)
        self.backgrounds['game']['forest'] = self.load_image(['backgrounds', 'game'], 'forest.png', transparent=False)
        self.backgrounds['game']['desert'] = self.load_image(['backgrounds', 'game'], 'desert.png', transparent=False)
        
        # Menu backgrounds
        self.backgrounds['menu']['main'] = self.load_image(['backgrounds', 'menu'], 'main_menu_background.png', transparent=False)
        self.backgrounds['menu']['theme'] = self.load_image(['backgrounds', 'menu'], 'menubg_test.jpg', transparent=False)
        self.backgrounds['menu']['skins'] = self.load_image(['backgrounds', 'menu'], 'menubg_test.jpg', transparent=False)
        
        # --- Obstacles ----
        # Statique
        # Cactus
        self.obstacles['statique']['cactus'] = []
        for i in range(6):
            self.obstacles['statique']['cactus'].append(
                self.load_image(['obstacles', 'statique', 'cactus'], f'{i}.png'))

        # A completer
            
            
        # Dynamique
        self.obstacles['dynamique']['oiseau'] = [self.load_image(['obstacles', 'dynamique', 'oiseau'], f'1.png'),
            self.load_image(['obstacles', 'dynamique', 'oiseau'], f'2.png')]
        
        # --- Other ----
        self.other['bullet'] = self.load_image(['other'], 'bullet.png')
        self.other['gun'] = self.load_image(['other'], 'gun.png')
        
        # --- Sons ---
        
        # A completer
        
        print("[AssetManager][Success] Assets charges!")

   