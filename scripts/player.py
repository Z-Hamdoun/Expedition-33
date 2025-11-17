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
        Initialise
        '''

        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 360))
        self.vel = 0
        self.acc = 0

        self.animations = {'jump': None,
            'run': None,
            'duck': None}
        
        """
        self.image = None
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        """
    
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
        hits = pygame.sprite.spritecollide(player,ground, False)
        if player.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1    
    
    def blit_me(self):
        ...
ground= pygame.sprite.Group()