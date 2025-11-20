import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    """Classe generale decrivant un obstacle tel un cactus ou un oiseau
    """
    def __init__(self, assets, settings, obs_type):
        super().__init__()
        self.settings = settings
        self.obs_type = obs_type
        
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
        if self.obs_type == 'oiseau':
            self.rect.x -= (self.settings.game_game_speed + 5)
        else:
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
        
        # Groupe de sprites pygame pour stocker tout les obstacles actifs et les powerups
        self.obstacles = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        
        self.spawn_timer = 0
        
        self.pattern_queue = [] # stoque les motifs d'obstacles

    def update(self):
        # Mettre a jour l'horloge
        self.spawn_timer -= 1
        
        # Spawn
        if self.spawn_timer <= 0:
            if not self.pattern_queue:
                self.generate_pattern()
                
            obs_type, gap_distance = self.pattern_queue.pop(0)
            
            if random.randint(1, 100) <= 40: 
                self.spawn_powerup()
                # Add a small gap after powerup so it's not unfair
                self.spawn_timer = 400 / self.settings.game_game_speed
            
            else:
                if obs_type == 'random':
                    obs_type = 'oiseau' if random.random() < 0.2 and self.settings.game_game_speed > 20 else 'cactus'

                # Ajouter l obstacle
                self.spawn_specific_obstacle(obs_type)
            
                # Trouver le temps avant le prochain spawn
                # si le motif n'est pas fini, utiliser un gap_distance
                if self.pattern_queue:
                    dist = gap_distance
                else:
                    # sinon prendre le game distance aleatoirement avant le prochain motif
                    min_gap = 1000
                    max_gap = 1200 + (self.settings.game_game_speed * 20) # Large variance makes it unpredictable
                    dist = random.randint(min_gap, int(max_gap))
            

                self.spawn_timer = dist / self.settings.game_game_speed
            
        # Mettre a jour tout les obstacles et les powerups dans le groupe
        self.obstacles.update()
        self.powerups.update()
    
    
    def generate_pattern(self):
        """Choisi un motif d'obstacles selon le game_speed"""
        patterns = []
        
        # --- motifs par defaut (n'import quelle vitesse) ---
        patterns.append([('random', 0)]) # un truc aleatoire
        patterns.append([('cactus', 0)]) # un cactus
        
        # --- Motifs plus difficiles (selon la vitesse) ---
        if self.settings.game_game_speed > 30:
            # Deux cactus proches
            patterns.append([('cactus', 280), ('cactus', 0)]) 
            
        if self.settings.game_game_speed > 10:
            # Deux oiseaux
            patterns.append([('oiseau', 400), ('oiseau', 0)])
            # Piege Oiseau + cactus
            patterns.append([('oiseau', 500), ('cactus', 0)])

        if self.settings.game_game_speed > 50:
            # 3 cactus
            patterns.append([('cactus', 300), ('cactus', 300), ('cactus', 0)])
            # 3 obstacles
            patterns.append([('cactus', 350), ('oiseau', 350), ('cactus', 0)])

        # Choix d'un pattern aleatoirement
        choice = random.choice(patterns)
        
        # Ajouter a la file
        self.pattern_queue.extend(choice)

    def spawn_specific_obstacle(self, type_name):
        new_obs = Obstacle(self.assets, self.settings, type_name)
        self.obstacles.add(new_obs)

    def draw(self, screen):
        # Dessiner tout les obstacles
        self.obstacles.draw(screen)
        self.powerups.draw(screen)
    
    def spawn_powerup(self):
        gun = GunPowerup(self.assets, self.settings)
        self.powerups.add(gun)

class GunPowerup(pygame.sprite.Sprite):
    def __init__(self, assets, settings):
        super().__init__()
        self.settings = settings
        
        img = assets.other['gun']
        self.image = pygame.transform.scale(img, (50, 50))

        self.rect = self.image.get_rect()
        
        # Position du spawn
        self.rect.x = 1920 + 50
        self.rect.bottom = settings.game_ground_y - random.choice([50, 150]) 

    def update(self):
        self.rect.x -= self.settings.game_game_speed
        
        # Despawn
        if self.rect.right < 0:
            self.kill()
