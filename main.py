import pygame
from scripts.player import Player
from pygame.locals import *
from scripts.scrollable_bg import *
import sys
import os
from scripts.obstacle import *
from random import randint

pygame.init()
vec = pygame.math.Vector2 
 
resolution = py.display.Info()
WIDTH, HEIGHT= resolution.current_w, resolution.current_h
ACC = 0.5
FPS = 60
obstacles = []

clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#definitions pour le background

largeur, hauteur = resolution.current_w, resolution.current_h
bg = background(img = os.path.join("assets/bg", "bg_test.png"))  #à changer plus tard avec le path du vrai bg


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
    bg.maj()
    bg.affiche(displaysurface)

    #partie obstacle
    if len(obstacles) == 0:
        nb = randint(0, 2)
        if nb == 0:
            obstacles.append(Oiseau())
        if nb == 1:
            obstacles.append(SmallCactus())
        if nb == 2:
            obstacles.append(LargeCactus())
    
    for obstacle in obstacles:
            obstacle.draw(displaysurface)
            obstacle.update(obstacles)
            #if player.dino_rect.colliderect(obstacle.rect):
            #    pygame.time.delay(2000)
            #    death_count += 1
            #    menu(death_count)
    

    inpt = pygame.key.get_pressed()
    #displaysurface.fill((255,255,255))
    player.blit_me(displaysurface)
    player.update(inpt)
    
    clock.tick(FPS)
    
    pygame.display.update()
        


