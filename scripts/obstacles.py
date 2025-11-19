import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    """Classe generale decrivant un obstacle tel un cactus ou un oiseau
    """
    def __init__(self, assets, settings, obs_type):
        super().__init__()
        self.settings = settings
        
        # Choix des images selon le type de l'obstacle
        if obs_type == "cactus":
            # Choisi un cactus aleatoire de la liste de cactus
            # assets.obstacles['statique']['nom obstacle'] est une liste d'image
            self.image = random.choice(assets.obstacles['statique']['cactus'])
            
            # On le place sur le sol
            self.rect = self.image.get_rect()
            self.rect.bottom = self.settings.game_ground_y
            
        elif obs_type == "oiseau":
            # A  changer pour qu'il y ai d'animations
            self.image = assets.obstacles['dynamique']['oiseau'][0]
            
            # Position: hautre aleatoire : Haut, moyen, bas
            self.rect = self.image.get_rect()
            # Decalage par rapport au niveau du sol
            height_offset = random.choice([50, 100, 20]) # on pourra ajouter ces parametres dans les parametres
            self.rect.bottom = self.settings.game_ground_y - height_offset

        # Spawn
        # on ajoute + 100 pour qu'il n'apparait pas instantannement
        
        ######## A CHANGER
        self.rect.x = 1920

    def update(self):
        # Bouge vers la gauche en utilisant la game_speed
        self.rect.x -= self.settings.game_game_speed

        # Despawn
        if self.rect.right < 0:
            self.kill()

class ObstacleManager:
    """Gestionnaire d'obstacles du jeu.
    """
    def __init__(self, assets, settings):
        self.assets = assets
        self.settings = settings
        
        # Groupe de sprites pygame pour stocker tout les obstacles actifs
        self.obstacles = pygame.sprite.Group()
        
        # Horloge
        self.spawn_timer = 0
        self.min_spawn_time = self.settings.game_fps  # 1 seconde
        self.max_spawn_time = 2 * self.settings.game_fps # 2 secondes

    def update(self):
        # Mettre a jour l'horloge
        self.spawn_timer -= 1
        
        # Spawn
        if self.spawn_timer <= 0:
            self.spawn_obstacle()
            # Reinitialiser l'horloge aleatoirement
            self.spawn_timer = random.randint(self.min_spawn_time, self.max_spawn_time)
            
        # Mettre a jour tout les obstacles dans le groupe
        self.obstacles.update()

    def spawn_obstacle(self):
        # Decide que spawn (par exemple 20% de chance pour Oiseau et 80% pour Cactus)
        if random.randint(1, 10) in [1, 2]:
            obs_type = "oiseau"
        else:
            obs_type = "cactus"
            
        # Creer l'objet et l'ajouter dans le groupe
        new_obs = Obstacle(self.assets, self.settings, obs_type)
        self.obstacles.add(new_obs)

    def draw(self, screen):
        # Dessiner tout les obstacles
        self.obstacles.draw(screen)
