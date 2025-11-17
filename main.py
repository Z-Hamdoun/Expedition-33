import pygame
from scripts.player import Player
from pygame.locals import *
from scripts.scrollable_bg import *
import sys

pygame.init()
vec = pygame.math.Vector2 
 
resolution = py.display.Info()
WIDTH, HEIGHT= resolution.current_w, resolution.current_h
ACC = 0.5
FPS = 60

dico_images = { 'Oiseau' : [pygame.image.load(os.path.join("assets/Bird", "Bird1.png"))],
                'LargeCactus' : [pygame.image.load(os.path.join("assets/Cactus","LargeCactus1")),pygame.image.load(os.path.join("assets/Cactus","LargeCactus2")),pygame.image.load(os.path.join("assets/Cactus","LargeCactus2"))],
                'SmallCactus' : [pygame.image.load(os.path.join("assets/Cactus","SmallCactus1")),pygame.image.load(os.path.join("assets/Cactus","SmallCactus2")),pygame.image.load(os.path.join("assets/Cactus","SmallCactus2"))]}


clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#definitions pour le background

largeur, hauteur = resolution.current_w, resolution.current_h
bg = background(img = 'bg_test.png')  #à changer plus tard avec le path du vrai bg


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

    #partie background
    clock.tick(60)
    for event in py.event.get():
        if event.type == QUIT:
            en_cours = False
    bg.maj()
    bg.affiche(displaysurface)
    py.display.flip()

        

    inpt = pygame.key.get_pressed()
    displaysurface.fill((255,255,255))
    player.blit_me(displaysurface)
    player.update(inpt)
    
    clock.tick(FPS)
    
    pygame.display.update()
        


