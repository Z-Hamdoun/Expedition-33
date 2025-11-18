import json


class Settings:
    """
    Classe permettant de gerer les parametres efficacement
    """
    def __init__(self):
        # Parametres par defaut
        
        # ------ Game ----------------
        self.game_fps = 60
        self.game_title = "Expedition 33"
        
        # ------ Player ----------
        self.player_jump_power = -16
        self.player_vitesse_limite = 15
        self.player_pos_initiale = (200, 500)
        
        # ------ Constants -------------
        self.constants_gravity = 0.8
        
        # Chargement des parametres
        self.load()
        
    
    def load(self):
        """Extrait les parametres a partir du fichier settings.json
        """
        try:
            with open('settings.json', 'r') as f:
                data = json.load(f)
                
                # Game settings
                data_game = data.get('game', {})
                self.game_fps = data_game.get('fps', 60)
                self.game_title = data_game.get('title', 'Expedition 33')
                self.high_score = data.get('high_score', 0)
                
                print("[Parametres] Parametres Charges")
                
        except FileNotFoundError:
            print("[Parametres] Fichier de parametres non trouve")
            self.save() # Create the file for next time
    
    def save_settings(self):
        """Sauvegarde les variables python dans le fichier settings.json"""
        
        data = {
            "game": {
                "fps" : 60,
                "title": "Expedition 33",
                "high_score": 0
            },
            "constants": {
                "GRAVITY": 0.8
            },
            "player": {
                "jump_power": -16,
                "vitesse_limite": 15,
                "pos_initiale": [200, 500]
            }
        }

        # Ecriture des donnees dans le fichier settings.json
        try:
            with open('settings.json', 'w') as f:
                # indent=4 pour rendre le fichier lisible
                json.dump(data, f, indent=4) 
                print("[Parametres] Sauvegarde de parametres terminee!")
        except IOError as e:
            print(f"[Parametres] Erreur: {e}")