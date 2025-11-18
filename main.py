import pygame
from scripts.player import Player
from pygame.locals import *
from scripts.scrollable_bg import *
import sys
import os
from scripts.obstacle import *
from random import randint
from scripts.menu import *

pygame.init()
vec = pygame.math.Vector2 
 
resolution = pygame.display.Info()
WIDTH, HEIGHT= resolution.current_w, resolution.current_h
ACC = 0.5
FPS = 60
obstacles = []

clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#definitions pour le background

bg = background(img = os.path.join("assets/bg", "bg_test.png"))  #à changer plus tard avec le path du vrai bg
player = Player()

menu_principal = MainMenu(WIDTH,HEIGHT,img = os.path.join("assets/bg", "menubg_test.jpg"))
jeu_actif = False
en_cours = True
boutons = {}

while en_cours:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if jeu_actif : jeu_actif = False
                else : en_cours = False
            if event.key == pygame.K_RETURN:
                jeu_actif = True
            if jeu_actif:
                if event.key == pygame.K_SPACE:
                    player.jump()
        if event.type == pygame.KEYUP:    
            if jeu_actif:
                if event.key == pygame.K_SPACE:
                    player.cancel_jump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #clic gauche
                if not jeu_actif :
                    if "start" in boutons and boutons["start"].collidepoint(event.pos):
                        jeu_actif = True
                    if "quitter" in boutons and boutons["quitter"].collidepoint(event.pos):
                        en_cours = False
                    if "options" in boutons and boutons["options"].collidepoint(event.pos):
                        print("bouton marche") # à coder après pur les thèmes

    if jeu_actif:
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

    else :
        boutons = menu_principal.affichage(displaysurface)


    clock.tick(FPS)
    pygame.display.update()


