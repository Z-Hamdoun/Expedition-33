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


clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_SPACE:
                player.cancel_jump()
        

    inpt = pygame.key.get_pressed()
    displaysurface.fill((255,255,255))
    player.blit_me(displaysurface)
    player.update(inpt)
    
    clock.tick(FPS)
    
    pygame.display.update()
        