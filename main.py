import pygame
from scripts.player import Player

pygame.init()
vec = pygame.math.Vector2 
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60


FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

player = Player()
