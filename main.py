import pygame
from scripts.player import Player
from pygame.locals import *
import sys

pygame.init()
vec = pygame.math.Vector2 
 
HEIGHT = 450
WIDTH = 700
ACC = 0.5
FPS = 60


FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_SPACE:
                player.cancel_jump()   

            
        displaysurface.fill((0,0,0))

    

    
        pygame.display.update()
        FramePerSec.tick(FPS)