import json


class Settings:
    """
    Classe permettant de gerer les parametres efficacement
    """
    def __init__(self):
        # Parametres par defaut
        
        # ------ Game ----------------
        self.debug_mode = False
        self.game_fps = 60
        self.game_title = "Expedition 33"
        self.game_high_score = 0
        self.game_ground_y = 600
        self.game_game_speed = 10
        self.game_mode = 'Facile'
        self.theme = "foret"
        self.game_acceleration = 0.5
        self.game_vmax = 40
        self.game_width = 1280
        self.game_height = 720
        
        # ------ Player ----------
        self.player_jump_power = -16
        self.player_vitesse_limite = 15
        self.player_pos_initiale = (200, 500)
        self.player_skin = 'forest'
        
        # ------ Constants -------------
        self.constants_gravity = 0.8
        
        # Chargement des parametres
        self.load()
        
    
    def load(self):
        """Extrait les parametres a partir du fichier settings.json
        """
        try:
            with open('config/settings.json', 'r') as f:
                data = json.load(f)
                
                # Game settings
                data_game = data.get('game', {})
                self.game_fps = data_game.get('fps', self.game_fps)
                self.game_title = data_game.get('title', self.game_title)
                self.high_score = data_game.get('high_score', self.game_high_score)
                self.game_ground_y = data_game.get('ground_y', self.game_ground_y)
                self.game_game_speed = data_game.get('game_speed', self.game_game_speed)
                self.game_mode = data_game.get('mode', self.game_mode)
                self.game_acceleration = data_game.get("acceleration", self.game_acceleration)
                self.game_vmax = data_game.get("vmax", self.game_vmax)
                self.theme = data_game.get("theme",self.theme)
                self.game_width = data_game.get("theme",self.game_width)  
                self.game_height = data_game.get("theme",self.game_height)

                # Player settings
                data_player = data.get('player', {})
                self.player_jump_power = data_player.get('jump_power', self.player_jump_power)
                self.player_vitesse_limite = data_player.get('vitesse_limite', self.player_vitesse_limite)
                self.player_pos_initiale = data_player.get('pos_initiale', self.player_pos_initiale)
                self.player_skin = data_player.get('skin', self.player_skin)
                
                # Constants
                data_constants = data.get('constants', {})
                self.constants_gravity = data_constants.get('gravity', self.constants_gravity)
                
                print("[Parametres] Parametres Charges")
                
        except FileNotFoundError:
            print("[Parametres] Fichier de parametres non trouve")
            self.save_settings() # Create the file for next time
    
    def save_settings(self):
        """Sauvegarde les variables python dans le fichier settings.json"""
        
        data = {
            "game": {
                "fps" : self.game_fps,
                "title": self.game_title,
                "high_score": self.game_high_score,
                "ground_y" : self.game_ground_y,
                "game_speed": self.game_game_speed,
                "width": self.game_width,
                "height": self.game_height,
                "mode": self.game_mode,
                "acceleration": self.game_acceleration,
                "vmax": self.game_vmax, 
            },
            "constants": {
                "gravity": self.constants_gravity
            },
            "player": {
                "jump_power": self.player_jump_power,
                "vitesse_limite": self.player_vitesse_limite,
                "pos_initiale": list(self.player_pos_initiale),
                "skin": self.player_skin
            }
        }

        # Ecriture des donnees dans le fichier settings.json
        try:
            with open('config/settings.json', 'w') as f:
                # indent=4 pour rendre le fichier lisible
                json.dump(data, f, indent=4) 
                print("[Parametres] Sauvegarde de parametres terminee!")
        except IOError as e:
            print(f"[Parametres] Erreur: {e}")