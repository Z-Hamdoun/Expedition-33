import pygame
from pygame.locals import *
from dimension import dimension

obstacles = []

HEIGHT = dimension()['HEIGHT']
WIDTH  = dimension()['WIDTH']

class Obstacle(pygame.sprite.Sprite):
    """ Classe générale dont vont hériter les différents obstacles"""
    def __init__(self,image):
        self.image = image
        super().__init__()
        self.rect = self.image.get_rect() 
        self.rect.x = WIDTH
    
    def update(self):
        self.rect.x -= 0 #Remplacer par le nom de la vitesse de jeu
        if self.rect.x < -self.rect.width:
            obstacles.pop()

class Oiseau(Obstacle):
    """Se baisser ou utiliser jet-pack pour l'éviter"""
    def __init__(self,image):
        super().__init__(image)
        self.rect.y = HEIGHT - 20

class Cactus(Obstacle):
    """Sauter par dessus"""
    def __init__(self,image):
        super().__init__(image)
        self.rect.y = 0

class Pics(Cactus):
    """Mettre un coup de griffe pour les passer"""
    def __init__(self,image):
        super().__init__(image)
        