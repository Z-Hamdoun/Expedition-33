import pygame

class GestionDifficulte():
    def __init__(self,vitesse0 = 10,acceleration = 0.5):
        self.vitesse0 = vitesse0
        self.acceleration = acceleration
        self.depart = 0

    def temps_depart(self):
        self.temps_depart = pygame.time.get_ticks()

    def maj(self):
        tps_ecoulé = (pygame.time.get_ticks() - self.depart)/1000 #conversion en secondes
        vitesse = min(self.vitesse0 + (tps_ecoulé * self.acceleration)/50 , 100)
        score = int(self.acceleration*tps_ecoulé*10)
        return vitesse,score


        