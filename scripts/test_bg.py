import pygame as py
from scrollable_bg import*
import os

resolution = py.display.Info()
largeur, hauteur = resolution.current_w, resolution.current_h
fenetre = py.display.set_mode((largeur, hauteur))

bg = background(img = os.path.join("assets/bg", "bg_test.png"))
clock = py.time.Clock()

joue = True

while joue:
    clock.tick(60)
    for event in py.event.get():
        if event.type == QUIT:
            en_cours = False
    bg.maj()
    bg.affiche(fenetre)
    py.display.flip()
py.quit()