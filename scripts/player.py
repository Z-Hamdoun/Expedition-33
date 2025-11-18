import pygame
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
        
        self.max_jump_speed = 8.5
        self.jump_speed = self.max_jump_speed
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
        self.rect: pygame.Rect = self.image.get_rect()
        # Valeurs initiales
        self.rect.x = 200
        self.rect.y = 500
        
        self.ground_y = 500
        self.duck_y = 560

        self.jumping = False
        self.ducking = False
        self.running = True
        
        # Variable qui gere l'animation running
        self.frame_number = 0
    
    def run(self):
        self.image = self.animations['running'][self.frame_number // 10] # change chaque 10 frames du jeu
        # Mise a jour du rect du joueur
        origin = self.rect.bottomleft
        self.rect = self.image.get_rect()
        self.rect.bottomleft = origin
        self.frame_number += 1
        
    def jump(self): 
        origin = self.rect.bottomleft
        self.image = self.animations['jumping']
        self.rect = self.image.get_rect()
        self.rect.bottomleft = origin
        if self.jumping:
            self.rect.y -= self.jump_speed * 4
            self.jump_speed -= 0.5
        if self.jump_speed < - self.max_jump_speed:
            self.jumping = False
            self.jump_speed = self.max_jump_speed
            
    def duck(self):
        self.image = self.animations['ducking'][self.frame_number // 10]
        if self.ducking:
            origin = self.rect.bottomleft
            self.rect = self.image.get_rect()
            self.rect.bottomleft = origin
            self.frame_number += 1

    def update(self, inpt: list):
        if self.frame_number >= 20:
            self.frame_number = 0
        
        if self.ducking:
            self.duck()
        elif self.running:
            self.run()
        elif self.jumping:
            self.jump()
        
        if inpt[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.running = False
            self.jumping = False
        elif inpt[pygame.K_UP] and not self.jumping:
            self.ducking = False
            self.running = False
            self.jumping = True
        elif not (self.jumping or inpt[pygame.K_DOWN]):
            self.ducking = False
            self.running = True
            self.jumping = False
 
    
    def blit_me(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))