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

from config.settings import Settings
from config.assets import AssetManager

pygame.init()

pygame.mixer.init()

music_game_file = os.path.join("Musiques", "Musique_thème_classique_Night_Drifting.mp3") 
music_menu_file = os.path.join("Musiques", "Musique_écran_acceuil.mp3") 
music_game_over_file = os.path.join("Musiques", "Musique_game_over.mp3") 

current_music = "" 

def play_music(file_path):
    global current_music
    if current_music == file_path:
        return
    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)
        current_music = file_path
    except pygame.error as e:
        print(f"ÉCHEC DE CHARGEMENT OU LECTURE DE LA MUSIQUE {file_path}: {e}")
        current_music = ""

play_music(music_menu_file)

resolution = pygame.display.Info()
WIDTH, HEIGHT = resolution.current_w, resolution.current_h
ACC = 0.5
obstacles = []
score = 0
best_score = 0   # BEST SCORE

score_police = pygame.font.Font(None, 60)
best_score_police = pygame.font.Font(None, 60)

clock = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

settings = Settings()
assets = AssetManager()

pygame.display.set_caption(settings.game_title)
difficulté = GestionDifficulte(settings.game_game_speed, 0.5)

bg = background(img=assets.backgrounds['background'])
player = Player(settings, assets)

menu_principal = MainMenu(WIDTH, HEIGHT, img=os.path.join("assets", "Backgrounds", "Menu", "menubg_test.jpg"))
menu_option = OptionMenu(WIDTH, HEIGHT, img=os.path.join("assets", "Backgrounds", "Menu", "menubg_test.jpg"))
menu_game_over = GameOverMenu(WIDTH, HEIGHT)
menu_pause = PauseMenu(WIDTH, HEIGHT)

jeu_actif = False
en_cours = True
etat_menu = "main"
boutons = {}

play_music(music_menu_file)

while en_cours:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
            settings.save_settings()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if jeu_actif:
                    jeu_actif = False
                    etat_menu = 'pause'
                    play_music(music_menu_file)
                elif etat_menu == 'option':
                    etat_menu = 'main'
                elif etat_menu == "main":
                    en_cours = False
                elif etat_menu == 'pause':
                    etat_menu = 'main'
                    jeu_actif = True
                    play_music(music_game_file)

        if event.type == pygame.KEYUP:
            if jeu_actif and event.key == pygame.K_UP:
                player.end_jump()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if not jeu_actif:

                if "start" in boutons and boutons["start"].collidepoint(event.pos):
                    jeu_actif = True
                    play_music(music_game_file)

                if "quitter" in boutons and boutons["quitter"].collidepoint(event.pos):
                    en_cours = False
                    settings.save_settings()

                if "options" in boutons and boutons["options"].collidepoint(event.pos):
                    etat_menu = "option"

                if "quitter_over" in boutons and boutons["quitter_over"].collidepoint(event.pos):
                    etat_menu = "main"
                    jeu_actif = False
                    play_music(music_menu_file)

                if "rejouer_over" in boutons and boutons["rejouer_over"].collidepoint(event.pos):
                    player, obstacles, bg = reinitialiser(settings)
                    score = 0
                    difficulté = GestionDifficulte(settings.game_game_speed, 0.5)
                    etat_menu = "main"
                    jeu_actif = True
                    play_music(music_game_file)

                if "quitter_pause" in boutons and boutons["quitter_pause"].collidepoint(event.pos):
                    etat_menu = "main"
                    jeu_actif = False

                if "reprendre" in boutons and boutons["reprendre"].collidepoint(event.pos):
                    etat_menu = "main"
                    jeu_actif = True
                    play_music(music_game_file)

                if "rejouer_pause" in boutons and boutons["rejouer_pause"].collidepoint(event.pos):
                    player, obstacles, bg = reinitialiser(settings)
                    score = 0
                    difficulté = GestionDifficulte(settings.game_game_speed, 0.5)
                    etat_menu = "main"
                    jeu_actif = True
                    play_music(music_game_file)

    if jeu_actif:
        play_music(music_game_file)
        
        vitesse_actuelle, score = difficulté.maj()

        bg.vitesse = vitesse_actuelle
        bg.maj()
        bg.affiche(displaysurface)

        if len(obstacles) == 0:
            nb = randint(0, 2)
            if nb == 0: obstacles.append(Oiseau())
            if nb == 1: obstacles.append(SmallCactus())
            if nb == 2: obstacles.append(LargeCactus())

        for obstacle in obstacles:
            obstacle.draw(displaysurface)
            obstacle.update(obstacles, vitesse_actuelle)

            if player.rect.colliderect(obstacle.rect):

                # Mise à jour du BEST SCORE
                if score > best_score:
                    best_score = score

                pygame.time.delay(300)
                obstacles = []
                jeu_actif = False
                etat_menu = "perdu"
                son = pygame.mixer.Sound(r"Sons\thème troll\Mort méchant dinosaure.mp3")
                son.play()
                play_music(music_game_over_file)

        inpt = pygame.key.get_pressed()
        player.blit_me(displaysurface)
        player.update(inpt)

        # Score
        displaysurface.blit(score_police.render(f'Score: {score}', True, (0, 0, 0)), (WIDTH - 250, 20))

        # Best Score (en jeu)
        displaysurface.blit(best_score_police.render(f'Best: {best_score}', True, (0, 0, 0)), (WIDTH - 250, 80))

    elif etat_menu == 'perdu':
        bg.affiche(displaysurface)
        for obstacle in obstacles:
            obstacle.draw(displaysurface)

        player.blit_me(displaysurface)

        boutons = menu_game_over.affichage(displaysurface, score)

        # BEST SCORE en jaune (+ position haute)
        displaysurface.blit(
            best_score_police.render(f'Best: {best_score}', True, (255, 255, 0)),
            (WIDTH / 2 - 100, HEIGHT / 2 - 100)
        )

    elif etat_menu == "pause":
        bg.affiche(displaysurface)
        for obstacle in obstacles:
            obstacle.draw(displaysurface)
        player.blit_me(displaysurface)
        boutons = menu_pause.affichage(displaysurface)

    else:
        play_music(music_menu_file)
        if etat_menu == "main":
            boutons = menu_principal.affichage(displaysurface)
        if etat_menu == "option":
            boutons = menu_option.affichage(displaysurface)

    clock.tick(settings.game_fps)
    pygame.display.update()




