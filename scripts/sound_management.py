import pygame
import os

class SoundManager:
    """
    Gère le chargement et la lecture de tous les sons et musiques du jeu.
    """
    def __init__(self):
        # S'assurer que pygame.mixer est initialisé
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        self.sounds = {} 
        self.musics = {
            "troll" : os.path.join("Musiques","Musique_thème_troll__Badali-Badala_.mp3"),
            "classique" : os.path.join("Musiques", "Musique_thème_classique_Night_Drifting.mp3"),
            "gameover" : os.path.join("Musiques", "Musique_game_over.mp3"),
            "accueil" : os.path.join("Musiques", "Musique_écran_acceuil.mp3")} 
        self.current_music = ""
        
        self.sound_paths = {
            "jump": os.path.join("sons", "jump.wav"), 
            "dino_death": os.path.join("sons", "mort.wav"),
            "pterodactyl": os.path.join("sons", "oiseau.wav"),
            "duck": os.path.join("sons", "duck.wav"),
            "gun": os.path.join("sons","tir.wav"),
            "recup" :  os.path.join("sons","recuperer.wav")
        }
        
        self.load_sounds()

    def load_sounds(self):
        """Charge tous les effets sonores (utilisent des Channel)."""
        print("Chargement des effets sonores (SFX)...")
        for name, path in self.sound_paths.items():
            try:
                # Charger le son
                self.sounds[name] = pygame.mixer.Sound(path)
                print(f"- Son '{name}' chargé : {path}")
            except pygame.error as e:
                print(f"Erreur de chargement du son '{name}' à '{path}': {e}")
                


    def play_sound(self, name):
        """Joue un effet sonore une seule fois."""
        if name in self.sounds:
            self.sounds[name].play()
        else:
            print(f"Erreur : Son SFX '{name}' non trouvé.")

    def play_music(self, name, loops=-1):
        """
        Charge et joue une musique en boucle (loops=-1 pour une boucle infinie). 
        Évite de recharger la même musique.
        """
        if name in self.musics:
            file_path = self.musics[name]
            
            # Si c'est déjà la musique jouée, ne fait rien
            if self.current_music == file_path:
                return
            
            # Sinon, arrête l'ancienne, charge et joue la nouvelle
            self.stop_music()
            try:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play(loops=loops)
                self.current_music = file_path
                print(f"Musique '{name}' lancée : {file_path}")
            except pygame.error as e:
                print(f"ÉCHEC DE CHARGEMENT OU LECTURE DE LA MUSIQUE {file_path}: {e}")
                self.current_music = ""
        else:
            print(f"Erreur : Nom de musique '{name}' non enregistré.")

    def stop_music(self):
        """Arrête la musique en cours."""
        pygame.mixer.music.stop()
        self.current_music = ""