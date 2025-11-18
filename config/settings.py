import json


class Settings:
    """
    Une classe pour gerer les parametres efficacement
    """
    def __init__(self):
        # Parametres par defaut
        
        
        # Chargement des parametres
        self.load()
        
    
    def load(self):
        """Extrait les parametres a partir du fichier settings.json
        """
        with open('settings.json', 'r') as f:
            data = json.load(f)