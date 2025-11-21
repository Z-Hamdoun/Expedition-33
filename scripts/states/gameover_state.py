import pygame
from scripts.states.state import State
from scripts.ui import Button
from scripts.sound_management import SoundManager

class GameOverState(State):
    def __init__(self, game, final_score = 100, prev_state = None):
        super().__init__(game)
        self.score = final_score
        self.font = pygame.font.Font(None, 60)
        
        # Previous state
        self.prev_state = prev_state
        
        # Transparent
        self.overlay = pygame.Surface((game.width, game.height))
        self.overlay.fill((255, 255, 255))
        self.overlay.set_alpha(180)

        # Bouttons
        cw, ch = game.width // 2, game.height // 2
        self.btn_replay = Button(cw, ch + 100, "Rejouer", self.font, (0,0,0), (255,215,0))
        self.btn_quit = Button(cw, ch + 200, "Quitter", self.font, (0,0,0), (255,215,0))

        #Musique
        self.sound = SoundManager()
        self.sound.play_music("gameover")

    def draw(self, surface):
        # Dessin de l'etat final
        if self.prev_state:
            self.prev_state.draw(surface)
            
        # Effet transparent
        surface.blit(self.overlay, (0, 0))
        
        # Afficher Text
        txt_surf = self.font.render("GAME OVER", True, (200, 50, 50))
        txt_rect = txt_surf.get_rect(center=(self.game.width//2, self.game.height//4))
        surface.blit(txt_surf, txt_rect)
        
        score_surf = self.font.render(f"Score: {self.score}", True, (200, 150, 50))
        score_rect = score_surf.get_rect(center=(self.game.width//2, self.game.height//2))
        surface.blit(score_surf, score_rect)

        # Draw Buttons
        self.btn_replay.draw(surface)
        self.btn_quit.draw(surface)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.btn_replay.update(mouse_pos)
        self.btn_quit.update(mouse_pos)

    def handle_input(self, events):
        for event in events:
            if self.btn_quit.is_clicked(event):
                # Revenir au Menu
                from scripts.states.menu_state import MenuState
                self.game.current_state = MenuState(self.game)
                
            if self.btn_replay.is_clicked(event):
                # Revenir au jeu
                from scripts.states.theme_state import ThemeState
                self.game.current_state = ThemeState(self.game)
    
    def desc(self):
        return 'game_over'