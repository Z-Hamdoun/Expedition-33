import pygame
import sys
import os
from pygame.math import Vector2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from config.settings import Settings

class Player(pygame.sprite.Sprite):
    '''
    Classe representant le joueur
    '''
    
    def __init__(self, settings: Settings):
        '''
        Initialise l'objet Player
        '''
        super().__init__()
        
        # Parametres du joueur
        self.settings = settings
        
        self.pos = Vector2(self.settings.player_pos_initiale().copy())
        self.vel = Vector2(0, 0)
        
        # Chargement des animations
        jumping = pygame.image.load(os.path.join("assets", "Dino", "DinoJump.png"))
        running = [pygame.image.load(os.path.join("assets", "Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("assets", "Dino", "DinoRun2.png"))]
        ducking = [pygame.image.load(os.path.join("assets", "Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("assets", "Dino", "DinoDuck2.png"))]
        
        # Charger les animations dans un dictionnaire
        self.animations = {'jumping': jumping,
            'running': running,
            'ducking': ducking}
        
        self.image = self.animations['running'][0]
        self.rect: pygame.Rect = self.image.get_rect()

        # Etat initial
        self.jumping = False
        self.ducking = False
        self.running = True
        
        # Variable qui gere l'animation running
        self.frame_number = 0
    
    
    def jump(self):
        """Permet au joueur de sauter
        """
        if self.pos.y >= self.settings.game_ground_y:
            self.vel.y = self.settings.player_jump_power
            self.jumping = True
            # Code pour ajouter du son !!
    
    def end_jump(self):
        """
        S'applique quand le joueur lache le boutton de saut
        """
        if self.vel.y < -5:
            self.vel.y *= 0.5
    
    def physics(self):
        """Gere la physique du joueur
        """
        self.vel.y += self.settings.constants_gravity
        if self.vel.y > self.settings.player_vitesse_limite:
            self.vel.y = self.settings.player_vitesse_limite
            

    def update(self, inpt: list):
        # Appliquer le PFD
        self.vel.y += self.settings.constants_gravity
        
        # Gerer les entrees du joueur
        self.handle_input(inpt)
        
        self.pos.y += self.vel.y
        
        # Detection de collision avec le sol
        if self.pos.y >= self.settings.game_ground_y:
            self.pos.y = self.settings.game_ground_y
            self.vel.y = 0
            self.running = True
        else:
            self.running = False
        
        self.update_animation()
        
        # Recentrer le joueur (evite les glitch)
        self.rect.midbottom = self.pos
    
    def handle_input(self, inpt):
        # Jumping
        if inpt[pygame.K_UP] and self.running:
            self.jump()
            self.running = False
        
        # Ducking
        if inpt[pygame.K_DOWN] and self.running:
            self.ducking = True
        else:
            self.ducking = False
    
    def update_animation(self):
        # Compteur de frames
        self.frame_number += 1
        if self.frame_number >= 20:
            self.frame_number = 0
        
        # Actualiser l'animation selon les frames
        if self.ducking:
            self.image = self.animations['ducking'][self.frame_number // 10]
        
            # Mise a jour du rect apres changement de l'animation
            self.rect = self.image.get_rect()

        elif self.jumping or not self.running:
            self.image = self.animations['jumping']
            self.rect = self.image.get_rect()

        else:
            frame_index = self.frame_number // 10
            self.image = self.animations['running'][frame_index % 2]
            self.rect = self.image.get_rect()
 
    
    def blit_me(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))