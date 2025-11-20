import pygame

class GestionDifficulte():
    def __init__(self,vitesse0 = 10,acceleration = 10,vmax = 40):
        self.vitesse0 = vitesse0
        self.acceleration = acceleration
        self.depart = 0
        self.vmax = vmax

    def reset_depart(self):
        self.depart = pygame.time.get_ticks()

    def update(self):
        tps_ecoulé = (pygame.time.get_ticks() - self.depart)/1000 #conversion en secondes
        vitesse = min(self.vitesse0 + (tps_ecoulé * self.acceleration) , self.vmax)
        score = int(self.acceleration*tps_ecoulé*10)
        return vitesse,score


        