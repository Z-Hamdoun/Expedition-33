import pygame
from pygame.math import Vector2
import os

class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos, assets):
        super().__init__()
        
        # Creer la surface Bullet
        # self.image = pygame.Surface((10, 10))
        # self.image.fill((255, 0, 0)) # Carre rouge pour le moment, a remplacer
        self.image = assets.other['bullet']
        self.rect = self.image.get_rect(center=start_pos)
        
        # Calculer le vecteur direction
        self.pos = Vector2(start_pos)
        target_vec = Vector2(target_pos)
        direction = target_vec - self.pos
        
        # Normalisation du vecteur
        if direction.length() > 0:
            direction = direction.normalize() 
        
        # Vitesse
        self.speed = 30
        self.velocity = direction * self.speed

    def update(self):
        # Faire bouger la bullet
        self.pos += self.velocity
        self.rect.center = self.pos
        
        # Tuer la balle si elle depasse l'ecran
        if not (0 <= self.rect.x <= 2000 and 0 <= self.rect.y <= 1200):
            self.kill()