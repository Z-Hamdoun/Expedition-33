class State:
    """Class abstraite modelisant un etat du jeu (menu, jeu, ...)
    """
    
    def __init__(self, game):
        self.game = game
        # Etat precedent, ca nous sera utile pour faire une pause screen
        self.prev_state = None 

    def update(self):
        """Fonction principale gerant l'etat
        """
        pass
    
    def draw(self, surface):
        """S'occupe de la partie graphique de l'etat
        """
        pass
    
    def handle_input(self, events):
        """Gestion des evenements pygame
        """
        pass
    
    def enter_state(self):
        """Applee quand on entre dans cet etat"""
        pass
    
    def exit_state(self):
        """Applee quand on quitte cet etat"""
        pass
    
    def desc(self):
        pass