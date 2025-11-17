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

dico_images = { 'Oiseau' : [pygame.image.load(os.path.join("assets/Bird", "Bird1.png"))],
                'LargeCactus' : [pygame.image.load(os.path.join("assets/Cactus","LargeCactus1")),pygame.image.load(os.path.join("assets/Cactus","LargeCactus2")),pygame.image.load(os.path.join("assets/Cactus","LargeCactus2"))],
                'SmallCactus' : [pygame.image.load(os.path.join("assets/Cactus","SmallCactus1")),pygame.image.load(os.path.join("assets/Cactus","SmallCactus2")),pygame.image.load(os.path.join("assets/Cactus","SmallCactus2"))]}


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

            
    displaysurface.fill((255,255,255))
    displaysurface.blit(player.image, (player.rect.x, player.rect.y))
    pygame.display.update()
    clock.tick(FPS)
        