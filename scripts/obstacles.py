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
            height_offset = random.choice([50, 100, 20])
            self.rect.bottom = self.settings.game_ground_y - height_offset

        # Spawn
        # on ajoute + 100 pour qu'il n'apparait pas instantannement
        self.rect.x = self.settings.game_width + 100

    def update(self):
        # Bouge vers la gauche en utilisant la game_speed
        self.rect.x -= self.settings.game_game_speed

        # Despawn
        if self.rect.right < 0:
            self.kill()


