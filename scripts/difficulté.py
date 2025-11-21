import pygame

class GestionDifficulte():
    def __init__(self,vitesse0 = 10,acceleration = 0.06,vmax = 40):
        self.vitesse0 = vitesse0
        self.acceleration = acceleration
        self.depart = 0
        self.vmax = vmax

    def reset_depart(self):
        self.depart = pygame.time.get_ticks()

    def update(self):
        tps_ecoulé = (pygame.time.get_ticks() - self.depart)/1000 #conversion en secondes
        if tps_ecoulé <= 30:
            vitesse = min(self.vitesse0 + (tps_ecoulé * self.acceleration) , 13)
        elif 30<tps_ecoulé<=60:
            vitesse = min(15 + ((tps_ecoulé-30) * self.acceleration) , 17)
        elif 60<tps_ecoulé<=90:
            vitesse = min(17 + ((tps_ecoulé-60) * self.acceleration) , 21)
        elif 90<tps_ecoulé<=120:
            vitesse = min(21 + ((tps_ecoulé-90) * self.acceleration) , 24)
        elif 120<tps_ecoulé:
            vitesse = min( 24 + ((tps_ecoulé-90) * self.acceleration) , 27)
        print(vitesse)
        score = int(self.acceleration*tps_ecoulé*10)
        return vitesse,score


        