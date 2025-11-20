## Description
Dino Runner est un jeu développé en Python avec Pygame, inspiré du jeu du dinosaure de Google Chrome. Le joueur contrôle un personnage capable de sauter, s'accroupir et tirer pour éviter ou détruire des obstacles, dans plusieurs thèmes graphiques et avec différents skins.
Ce projet a été réalisé dans le cadre d’un travail collaboratif organisé en sprints, en utilisant Git comme outil de travail.

## Présentation
Dino Runner est un runner en 2D où le joueur doit éviter les obstacles, survivre le plus longtemps possible, et progresser dans un environnement dynamique.
Le jeu inclut différents thèmes, un système complet de tir, plusieurs obstacles, des sons, des menus, ainsi qu’un système de score.

## Equipe
Membres de l'équipe et rôles:
- Arthur HAKIMI: Implémentation des obstacles
- Arthur LENHARDT : Intégration sons & musiques
- Ghali BENJELLOUN : Graphismes & documentation
- Deyaa-Eddine NACIRI : Menus & thèmes
- Hugo FOURNIER : Implémentation du player
- Zakaria HAMDOUN : Structure globale & debugging

## Fonctionnalités
Gameplay : 
- Saut (↑)
- Accroupissement (↓)
- Tir avec le clic gauche de la souris
- Apparition d’armes dans le jeu
- Collisions et obstacles variés

Graphisme et thèmes : 
- Thèmes graphiques intégrés (désert, forêt, etc.)
- Skins personnalisables
- Sprites adaptés automatiquement au thème choisi

Audio : 
- Sons d’action : saut, course, tir…
- Musiques d’ambiance
- Gestion complète via un Sound Manager

Interface et menus : 
- Menu principal
- Menu des skins
- Choix des thèmes
- Pause / Game Over

Architecture et Organisation : 
- Création de modules 
- Réalisation de tests 
- Refactoring en profondeur (sprint 3)

## Stucture du projet 
ProjetDino/
│-- assets/
│   ├── Backgrounds/
│   ├── Dino/
│   └── obstacles/
│
│-- scripts
│   ├── states/
│   ├── Test/
│   ├── obstacles.py
│   ├── bullet.py
│   ├── menu.py
│   ├── game.py
│   └── player.py
    ├── others.py
│   ├── scrollable_bg.py
│   ├── sound_management.py
│   └── ui.y
│
└── README.md
└── main_fix.py

## Déroulement du développement
Sprint 1 — Base du jeu : 
- Création du personnage
- Saut et accroupissement
- Obstacles de base

Sprint 2 — Gameplay avancé:
- Nouveaux obstacles
- Amélioration des collisions

Sprint 3 — Refactoring, thèmes & interface:
- Refactoring complet de main.py
- Correction de bugs
- Obstacles dépendant du thème (cactus / arbres…)
- Ajout du sol
- Sons d’action (saut, course…)
- Amélioration du GUI

Sprint 4 — Pistolet, nouvel ennemi & menus: 
- Ajout d’un premier pistolet
- Mécanisme de tir 
- Implémentation des skins dans les menus
- Choix des thèmes depuis les menus

Sprint 5 — Menus avancés, difficulté & polish:
- Menu des skins finalisé
- Sprites de skins créés
- Apparition d’armes en jeu
- Sprite du pistolet
- Logique des thèmes finalisée
- Corrections de bugs

Sprint 6 — Tests, nouveaux ennemis & finitions:
- Testing global & tuning des paramètres
- Ajout d’un nouvel ennemi supplémentaire
- Sprites adaptés selon le thème (obstacles, oiseaux…)
- Sound Manager intégré partout
- Polishing & corrections finales


## Références 
https://chromedino.com/
https://github.com/MaxRohowsky/chrome-dinosaur/blob/master/main.py

