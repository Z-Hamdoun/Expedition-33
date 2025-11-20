import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    """Classe generale decrivant un obstacle tel un cactus ou un oiseau
    """
    def __init__(self, assets, settings, obs_type):
        super().__init__()
        self.settings = settings
        
        # Variables d'animation
        self.is_animated = False
        self.frame_index = 0
        self.animation_speed = 0.15 # Vitesse de battement des ailes
        
        # Choix des images selon le type de l'obstacle
        if obs_type == "cactus":
            # Choisi un cactus aleatoire de la liste de cactus
            # assets.obstacles['statique']['nom obstacle'] est une liste d'image
            self.image = random.choice(assets.obstacles['statique']['cactus'])
            
            # On le place sur le sol
            self.rect = self.image.get_rect()
            self.rect.bottom = self.settings.game_ground_y
            
        elif obs_type == "oiseau":
            self.is_animated = True
            # A  changer pour qu'il y ai d'animations
            self.frames = assets.obstacles['dynamique']['oiseau']
            self.image = self.frames[0]
            
            # Position: hautre aleatoire : Haut, moyen, bas
            self.rect = self.image.get_rect()
            # Decalage par rapport au niveau du sol
            height_offset = random.choice([20, 90, 150]) # on pourra ajouter ces parametres dans les parametres
            self.rect.bottom = self.settings.game_ground_y - height_offset

        # Spawn
        # on ajoute + 100 pour qu'il n'apparait pas instantannement
        
        ######## A CHANGER
        self.rect.x = 1920 + 50

    def update(self):
        # Animation
        self.update_animation()
        
        # Bouge vers la gauche en utilisant la game_speed
        self.rect.x -= self.settings.game_game_speed

        # Despawn
        if self.rect.right < 0:
            self.kill()
    
    def update_animation(self):
        if self.is_animated:
            self.frame_index += self.animation_speed
            # Boucle sur les frames (modulo)
            if self.frame_index >= len(self.frames):
                self.frame_index = 0
            
            self.image = self.frames[int(self.frame_index)]
            # Mettre a jour le mask
            self.mask = pygame.mask.from_surface(self.image)

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
            
            min_dist = 1000  # Distance minimale entre deux obstacles
            max_dist = 1000 + (self.settings.game_game_speed * 10) # Plus on va vite, plus l'ecart max augmente
            
            rand_dist = random.randint(min_dist, int(max_dist))
            

            self.spawn_timer = rand_dist / self.settings.game_game_speed
            
        # Mettre a jour tout les obstacles dans le groupe
        self.obstacles.update()

    def spawn_obstacle(self):
        # Au debut (vitesse lente), peu d'oiseaux
        
        bird_chance = 10 # 10% de chance initiale
        
        if self.settings.game_game_speed > 20:
            bird_chance = 25 # 25% 
        if self.settings.game_game_speed > 80:
            bird_chance = 40 # 40% 

        # Tirage aleatoire
        tirage = random.randint(1, 100)
        
        if tirage <= bird_chance:
            obs_type = "oiseau"
        else:
            obs_type = "cactus"
            
        new_obs = Obstacle(self.assets, self.settings, obs_type)
        self.obstacles.add(new_obs)

    def draw(self, screen):
        # Dessiner tout les obstacles
        self.obstacles.draw(screen)
