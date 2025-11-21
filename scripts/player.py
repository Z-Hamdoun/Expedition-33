import pygame
import sys
import os
from pygame.math import Vector2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from scripts.bullet import Bullet
from scripts.sound_management import SoundManager
from config.settings import Settings
from config.assets import AssetManager


class Player(pygame.sprite.Sprite):
    '''
    Classe representant le joueur
    '''
    
    def __init__(self, settings: Settings, assets: AssetManager):
        '''
        Initialise l'objet Player
        '''
        super().__init__()
        
        # Parametres du joueur
        self.settings = settings
        self.assets = assets
        
        self.pos = Vector2(self.settings.player_pos_initiale.copy())
        self.vel = Vector2(0, 0)
        
        # Charger les animations dans un dictionnaire
        self.animations = {'jumping': self.assets.skins[self.settings.player_skin]['jump'],
            'running': self.assets.skins[self.settings.player_skin]['run'],
            'ducking': self.assets.skins[self.settings.player_skin]['duck']}
        
        self.image = self.animations['running'][0]
        self.rect: pygame.Rect = self.image.get_rect()
        self.sound = SoundManager()
        # Etat initial
        self.jumping = False
        self.ducking = False
        self.running = True
        
        # Variable qui gere l'animation running
        self.frame_number = 0

        # Gestion de l'ammunition
        self.max_ammo = 3
        self.current_ammo = 0
        self.last_shot_time = 0
        self.shoot_delay = 1000 # 1 secondes entre deux tirs
        
        self.has_gun = False

        # Hitting
        self.attacking = False
    
    def jump(self):
        """
        Permet au joueur de sauter
        """
        if self.pos.y >= self.settings.game_ground_y:
            self.vel.y = self.settings.player_jump_power
            self.jumping = True

    
    def end_jump(self):
        """
        S'applique quand le joueur lache le boutton de saut
        """
        if self.vel.y < -5:
            self.vel.y *= 0.5
    
    def physics(self):
        """Gere la physique du joueur
        """
        self.vel.y += self.settings.constants_gravity
        if self.vel.y > self.settings.player_vitesse_limite:
            self.vel.y = self.settings.player_vitesse_limite
    
    def _can_shoot(self):
        """Gere la logique du tir"""
        current_time = pygame.time.get_ticks()
        ready = self.has_gun and self.current_ammo > 0
        cooldown_ready = (current_time - self.last_shot_time >= self.shoot_delay)
        return ready and cooldown_ready

    def equip_gun(self):
        """Appelee quand le joueur recupere le pistolet"""
        self.has_gun = True
        self.current_ammo = self.max_ammo

    def _shoot(self):
        """Mets a jour les variables apres un tir"""
        self.current_ammo -= 1
        self.last_shot_time = pygame.time.get_ticks()
        self.last_reload_time = self.last_shot_time 
        if self.current_ammo <= 0:
            self.has_gun = False
            

    def update(self, inpt: list):
        # Appliquer le PFD
        self.vel.y += self.settings.constants_gravity
        
        # Gerer les entrees du joueur
        self.handle_input(inpt)
        
        self.pos.y += self.vel.y
        
        # Detection de collision avec le sol
        if self.pos.y >= self.settings.game_ground_y:
            self.pos.y = self.settings.game_ground_y
            self.vel.y = 0
            self.running = True
            self.jumping = False
        else:
            self.running = False
        
        self.update_animation()
        
        # Recentrer le joueur (evite les glitch)
        self.rect.midbottom = self.pos
    
    def handle_input(self, inpt):
        # Jumping
        if inpt[pygame.K_z] and self.running:
            self.jump()
            self.sound.play_sound("jump")
            self.running = False
        
        # Ducking
        if inpt[pygame.K_s] and self.running:
            self.ducking = True
            # self.sound.play_sound("duck")
        else:
            self.ducking = False
        
        if inpt[pygame.K_s] and not self.running and not inpt[pygame.K_z]:
            if self.vel.y < 0:
                self.vel.y = 2
    
    def update_animation(self):
        # Compteur de frames
        self.frame_number += 1
        if self.frame_number >= 20:
            self.frame_number = 0
        
        # Actualiser l'animation selon les frames
        if self.ducking:
            self.image = self.animations['ducking'][self.frame_number // 10]
        
            # Mise a jour du rect apres changement de l'animation
            self.rect = self.image.get_rect()

        elif self.jumping or not self.running:
            self.image = self.animations['jumping']
            self.rect = self.image.get_rect()

        elif self.running:
            self.image = self.animations['running'][self.frame_number // 10]
            self.rect = self.image.get_rect()
    
    def blit_me(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        if self.has_gun:
            gun_img = self.assets.other.get('gun')
            gun_img = pygame.transform.scale(gun_img, (50, 50)) 
            
            if gun_img:
                gun_x = self.rect.centerx + 10
                gun_y = self.rect.centery - 30
                
                # Ajustement pour ducking
                if self.ducking:
                    gun_y += 5
                    gun_x -= 10 
                
                if self.running and not self.ducking:
                    bob_offset = 2 if int(self.frame_number) // 10 == 0 else -2
                    gun_y += bob_offset
                
                screen.blit(gun_img, (gun_x, gun_y))