import pygame
from scripts.player import Player
from pygame.locals import *
from scripts.scrollable_bg import *
import sys
import os
from scripts.obstacle import *
from random import randint
from scripts.menu import *
from scripts.reset import *
from scripts.difficulté import *

pygame.init()

pygame.mixer.init()

music_game_file = os.path.join("Musiques", "Musique_thème_classique_Night_Drifting.mp3") 
music_menu_file = os.path.join("Musiques", "Musique_écran_acceuil.mp3") 
music_game_over_file = os.path.join("Musiques", "Musique_game_over.mp3") 

# Variable pour suivre quelle musique est censée jouer
current_music = "" 

def play_music(file_path):
    global current_music
    if current_music == file_path:
        return
    # Arrête la musique en cours
    pygame.mixer.music.stop()
    try:
        # Charge et joue la nouvelle musique en boucle
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)
        current_music = file_path
    except pygame.error as e:
        print(f"ÉCHEC DE CHARGEMENT OU LECTURE DE LA MUSIQUE {file_path}: {e}")
        current_music = ""

play_music(music_menu_file)

vec = pygame.math.Vector2 
 
resolution = pygame.display.Info()
WIDTH, HEIGHT= resolution.current_w, resolution.current_h
ACC = 0.5
FPS = 60
obstacles = []
game_speed = 10 # 6.5
vmax = 40
acceleration = 0.5
mode = "Moyen"
vitesse_actuelle = game_speed
difficulté = GestionDifficulte(game_speed,acceleration)
score = 0
score_police = pygame.font.Font(None, 60)

clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#definitions pour le background

bg = background(img = os.path.join("assets", "Backgrounds", "Game", "tall_trees.png"))  #à changer plus tard avec le path du vrai bg
player = Player()

menu_principal = MainMenu(WIDTH,HEIGHT,img = os.path.join("assets", "Backgrounds", "Menu", "menubg_test.jpg"))
menu_option = OptionMenu(WIDTH,HEIGHT,img = os.path.join("assets", "Backgrounds", "Menu", "menubg_test.jpg"))
menu_game_over = GameOverMenu(WIDTH,HEIGHT)
menu_pause = PauseMenu(WIDTH,HEIGHT) 
jeu_actif = False
en_cours = True
etat_menu = "main"
boutons = {}

# Lancement initial de la musique du menu 
play_music(music_menu_file)


while en_cours:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if jeu_actif :
                    jeu_actif = False
                    etat_menu = 'pause'
                    play_music(music_menu_file) 
                elif etat_menu == 'option' :
                    etat_menu = 'main'
                elif etat_menu == "main" :
                    en_cours = False
                elif etat_menu == 'pause':
                    etat_menu = 'main'
                    jeu_actif = True
                    play_music(music_game_file)

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
                        difficulté.reset_depart()
                        jeu_actif = True
                        play_music(music_game_file)
                    if "quitter" in boutons and boutons["quitter"].collidepoint(event.pos):
                        en_cours = False
                    if "options" in boutons and boutons["options"].collidepoint(event.pos):
                        etat_menu = "option"
                    if "quitter_over" in boutons and boutons["quitter_over"].collidepoint(event.pos):
                        etat_menu = "main"
                        jeu_actif = False
                        player, obstacles, bg, score = reinitialiser()
                        difficulté.reset_depart()
                        vitesse_actuelle = game_speed
                        play_music(music_menu_file) 
                    if "rejouer_over" in boutons and boutons["rejouer_over"].collidepoint(event.pos):
                        player, obstacles, bg, score = reinitialiser()
                        vitesse_actuelle = game_speed
                        difficulté.reset_depart()
                        etat_menu = "main"
                        jeu_actif = True
                        play_music(music_game_file)

                    if "quitter_pause" in boutons and boutons["quitter_pause"].collidepoint(event.pos):
                        etat_menu = "main"
                        jeu_actif = False
                        player, obstacles, bg, score = reinitialiser()
                        difficulté.reset_depart()
                        vitesse_actuelle = game_speed
                    if "reprendre" in boutons and boutons["reprendre"].collidepoint(event.pos):
                        etat_menu = "main" 
                        jeu_actif = True
                        play_music(music_game_file)
                    if "rejouer_pause" in boutons and boutons["rejouer_pause"].collidepoint(event.pos):
                        player, obstacles, bg, score = reinitialiser()
                        vitesse_actuelle = game_speed
                        difficulté.reset_depart()
                        etat_menu = "main"
                        jeu_actif = True
                        play_music(music_game_file)
                    if "Facile" in boutons and boutons["Facile"].collidepoint(event.pos):
                        game_speed = 5
                        difficulté.vmax = 20
                        difficulté.acceleration = 0.3
                        difficulté.vitesse0 = game_speed
                        mode = "Facile"
                    if "Moyen" in boutons and boutons["Moyen"].collidepoint(event.pos):
                        game_speed = 10
                        difficulté.vmax = 40
                        difficulté.acceleration = 0.5
                        difficulté.vitesse0 = game_speed
                        mode = "Moyen"
                    if "Difficile" in boutons and boutons["Difficile"].collidepoint(event.pos):
                        game_speed = 15
                        difficulté.vmax = 60
                        difficulté.acceleration = 0.7
                        difficulté.vitesse0 = game_speed
                        mode = "Difficile"



    if jeu_actif:
        play_music(music_game_file)
        difficulté.vitesse0 = game_speed
        difficulté.vmax = vmax
        difficulté.acceleration = acceleration
        vitesse_actuelle,score = difficulté.maj()
        #partie background
        bg.vitesse = vitesse_actuelle
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
                obstacle.update(obstacles,vitesse_actuelle)
                if player.rect.colliderect(obstacle.rect):
                    pygame.time.delay(300)
                    obstacles = []
                    jeu_actif = False
                    etat_menu = "perdu"
                    play_music(music_game_over_file)

        

        inpt = pygame.key.get_pressed()
        player.blit_me(displaysurface)
        player.update(inpt)

        displaysurface.blit(score_police.render(f'Score: {score}', True, (0, 0, 0)),(WIDTH - 250, 20))

    elif etat_menu == 'perdu':
        # Écran Game Over.
        bg.affiche(displaysurface)
        for obstacle in obstacles:
            obstacle.draw(displaysurface)
        player.blit_me(displaysurface)
        boutons  = menu_game_over.affichage(displaysurface,score)

    elif etat_menu == "pause":
        bg.affiche(displaysurface)
        for obstacle in obstacles:
            obstacle.draw(displaysurface)
        player.blit_me(displaysurface)
        boutons  = menu_pause.affichage(displaysurface)
        
    else :
        play_music(music_menu_file) 
        
        if etat_menu == "main":
            boutons = menu_principal.affichage(displaysurface)
        if etat_menu == "option":
            boutons = menu_option.affichage(displaysurface,mode)


    clock.tick(FPS)
    pygame.display.update()