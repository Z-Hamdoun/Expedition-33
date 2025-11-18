import json


class Settings:
    """
    Une classe pour gerer les parametres efficacement
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
        with open('settings.json', 'r') as f:
            data = json.load(f)
            
            # Game settings
            data_game = data.get('game', {})
            self.game_fps = data_game.get('fps', 60)
            self.game_title = data_game.get('title', 'Expedition 33')
            self.high_score = data.get('high_score', 0)
            
            print("Parametres Charges")
                