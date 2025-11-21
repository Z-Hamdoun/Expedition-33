import pygame
import random
import math

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
            self.is_shootable = False
            # Choisi un cactus aleatoire de la liste de cactus
            # assets.obstacles['statique']['nom obstacle'] est une liste d'image
            self.image = random.choice(assets.obstacles['statique']['cactus'])
            
            # On le place sur le sol
            self.rect = self.image.get_rect()
            self.rect.bottom = self.settings.game_ground_y
            
        elif obs_type == "oiseau":
            self.is_animated = True
            self.is_shootable = True
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
        self.rect.x = settings.game_width + 50

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

class JumpingEnemy(pygame.sprite.Sprite):
    """Ennemi qui saute vers la gauche"""
    def __init__(self, assets, settings):
        super().__init__()
        self.settings = settings
        self.is_shootable = True
        
        # Partie graphique
        self.image = pygame.Surface((40, 40))
        self.image.fill((50, 205, 50)) # Vert
            
        pygame.draw.circle(self.image, (255, 255, 255), (10, 10), 5)
        pygame.draw.circle(self.image, (255, 255, 255), (30, 10), 5)

        self.rect = self.image.get_rect()
        
        # logique spawn 
        self.rect.x = settings.game_width + 50
        self.rect.bottom = settings.game_ground_y
        
        # Physique
        self.vel_y = 0
        self.gravity = 0.6      # gravite differente de celle du joueur
        self.jump_power = -20

    def update(self):
        # Vers la gauche
        self.rect.x -= self.settings.game_game_speed
        
        # Direction verticale
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        
        # Collision et rebondissement
        if self.rect.bottom >= self.settings.game_ground_y:
            self.rect.bottom = self.settings.game_ground_y
            self.vel_y = self.jump_power 

        # Despawn
        if self.rect.right < 0:
            self.kill()

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
            
            if random.randint(1, 100) <= 5: 
                self.spawn_powerup()
                # Add a small gap after powerup so it's not unfair
                self.spawn_timer = 400 / self.settings.game_game_speed
            
            else:
                if obs_type == 'random':
                    tirage = random.random()
                    if tirage < 0.2 and self.settings.game_game_speed > 10:
                        obs_type = 'oiseau'
                    elif tirage < 0.3 and self.settings.game_game_speed > 10:
                        obs_type = 'jumping_enemy'
                    else:
                        obs_type = 'cactus'

                # Ajouter l obstacle
                self.spawn_specific_obstacle(obs_type)
            
                # Trouver le temps avant le prochain spawn
                # si le motif n'est pas fini, utiliser un gap_distance
                if self.pattern_queue:
                    dist = gap_distance
                else:
                    # sinon prendre le game distance aleatoirement avant le prochain motif
                    min_gap = 1000
                    max_gap = 1200 + (self.settings.game_game_speed * 20)
                    dist = random.randint(min_gap, int(max_gap))
            

                self.spawn_timer = dist / self.settings.game_game_speed
            
        # Mettre a jour tout les obstacles et les powerups dans le groupe
        self.obstacles.update()
        self.powerups.update()
    
    
    def generate_pattern(self):
        """Choisi un motif d'obstacles selon le game_speed"""
        patterns = []
        
        # --- NIVEAU 0: WARMUP (Speed < 16) ---
        # Mostly random single obstacles to get used to the speed
        patterns.append([('random', 0)]) 
        patterns.append([('cactus', 0)])
        
        # --- NIVEAU 1: RHYTHME (Speed 14 - 17) ---
        # Motifs basiques
        if 14<= self.settings.game_game_speed <= 17:
            # double cactus
            patterns.append([('cactus', 380), ('cactus', 0)]) 
            
            # Oiseau + cactus
            patterns.append([('oiseau', 400), ('cactus', 0)]) 

        # --- NIVEAU 2: PRECISION (Speed 17 - 21) ---
        # Plus de rapidite
        if self.settings.game_game_speed >= 17:
            # Cactus puis frog
            patterns.append([('cactus', 520), ('jumping_enemy', 0)])
            
            # "Duck and Cover": Deux oiseaux
            # Duck -> Jump 
            patterns.append([('oiseau', 400), ('oiseau', 0)])

        # --- NIVEAU 3: Pieges (Speed 21 - 24) ---
        # Mental load increases. You have to identify threats quickly.
        if self.settings.game_game_speed >= 21:
            # "Le MUR" 3 cactus
            patterns.append([('cactus', 500), ('cactus', 70), ('cactus', 0)])
            
            # Frog + bird
            patterns.append([('jumping_enemy', 450), ('oiseau', 0)])
            
            # Jeu de tirs 
            patterns.append([('oiseau', 400), ('jumping_enemy', 400), ('oiseau', 0)])

        # --- NIVEAU 4: CHAOS (Speed 24+) ---
        if self.settings.game_game_speed >= 24:
            # 4 obstacles. 
            # Cactus -> (fast jump) -> Cactus -> (duck) -> Bird -> (shoot/jump) -> Frog
            patterns.append([('cactus', 700), ('cactus', 500), ('oiseau', 400), ('jumping_enemy', 0)])
            
            # 3 oiseaux
            patterns.append([('oiseau', 400), ('oiseau', 450), ('oiseau', 0)])

        # --- MAX SPEED (Speed 27+) ---
        if self.settings.game_game_speed >= 27:
            # mode panique: RANDOM
            patterns.append([('random', 700), ('random', 500), ('random', 600)])

        # Choix d'un pattern aleatoirement
        choice = random.choice(patterns)
        
        # Ajouter a la file
        self.pattern_queue.extend(choice)

    def spawn_specific_obstacle(self, type_name):
        if type_name == 'jumping_enemy':
            new_obs = JumpingEnemy(self.assets, self.settings)
        else:
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
        self.rect.x = settings.game_width + 50
        self.base_y = settings.game_ground_y - random.choice([50, 150]) 
        self.rect.centery = self.base_y
        
        # Variables d'animation
        self.hover_timer = 0
        self.hover_speed = 0.05  # frequence d oscillation
        self.hover_amount = 10   # Amplitude

    def update(self):
        self.rect.x -= self.settings.game_game_speed
        
        # Animation
        self.hover_timer += self.hover_speed
        offset = math.sin(self.hover_timer) * self.hover_amount
        self.rect.centery = self.base_y + offset
        
        # Despawn
        if self.rect.right < 0:
            self.kill()
