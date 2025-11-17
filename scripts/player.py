import pygame
from pygame.locals import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))



vec = pygame.math.Vector2 



class Player:
    '''
    Classe representant le joueur
    '''
    
    def __init__(self):
        '''
        Initialise l'objet Player
        '''
        
        self.vel = 0
        self.acc = 0
        
        # Chargement des animations
        jumping = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))
        running = [pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png"))]
        ducking = [pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png"))]
        
        # Charger les animations dans un dictionnaire
        self.animations = {'jumping': jumping,
            'running': running,
            'ducking': ducking}
        
        self.image = self.animations['running'][0]
        self.rect = self.image.get_rect()
        # Valeurs initiales
        self.rect.x = 100
        self.rect.y = 200
        
        self.jumping = False
        self.ducking = False
        self.running = True
    
    def run(self):
        self.acc = 0.5
        self.vel += self.acc
        self.pos.y += self.vel + 0.5 * self.acc
        
    def jump(self): 
        hits = pygame.sprite.spritecollide(self, ground, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -15
    
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
    def update(self):
        if self.ducking
        if self.vel > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1    
    
    def blit_me(self):
        ...
ground= pygame.sprite.Group()