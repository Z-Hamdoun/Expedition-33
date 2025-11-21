import pygame
from scripts.states.state import State
from scripts.ui import Button
from scripts.sound_management import SoundManager

class PauseState(State):
    def __init__(self, game, prev_state):
        super().__init__(game)
        self.prev_state = prev_state # This holds the frozen PlayState
        
        self.game = game
        
        # Transparent Overlay
        self.overlay = pygame.Surface((game.height//2, 3*game.width//8))
        self.overlay.fill((0, 0, 0)) # Black overlay
        self.overlay.set_alpha(128)  # 50% Darker
        self.overlay_rect = self.overlay.get_rect()
        self.overlay_rect.center = (game.width//2, game.height//2)

        # Fonts
        self.font = pygame.font.Font(None, 60)
        
        # Buttons
        cw, ch = game.width // 2, game.height // 2
        self.btn_resume = Button(cw, ch - 80, "Reprendre", self.font, (255,255,255), (255,215,0))
        self.btn_menu = Button(cw, ch + 80, "Menu Principal", self.font, (255,255,255), (255,215,0))
        self.btn_rejouer = Button(cw, ch, 'Rejouer',self.font, (255,255,255), (255,215,0))

        self.sound = SoundManager()
        #self.sound.play_music("accueil")
    def update(self):
        # We do NOT call self.prev_state.update()
        # This effectively "Freezes" the game logic!
        
        mouse_pos = pygame.mouse.get_pos()
        self.btn_resume.update(mouse_pos)
        self.btn_rejouer.update(mouse_pos)
        self.btn_menu.update(mouse_pos)

    def draw(self, surface):
        # 1. Draw the frozen game first
        self.prev_state.draw(surface)
        
        # 2. Draw the dark overlay
        surface.blit(self.overlay,self.overlay_rect)
        
        # 3. Draw UI
        title = self.font.render("PAUSE", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.game.width//2, self.game.height//4))
        surface.blit(title, title_rect)
        
        self.btn_resume.draw(surface)
        self.btn_rejouer.draw(surface)
        self.btn_menu.draw(surface)

    def handle_input(self, events):
        for event in events:
            # Button: Resume
            if self.btn_resume.is_clicked(event):
                # Go back to the previous state (The Game)
                self.game.current_state = self.prev_state
                
            # Button: Menu
            if self.btn_menu.is_clicked(event):
                from scripts.states.menu_state import MenuState
                self.game.current_state = MenuState(self.game)
            
            if self.btn_rejouer.is_clicked(event):
                from scripts.states.theme_state import ThemeState
                self.game.current_state = ThemeState(self.game)

            # Key: ESC to Resume
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.current_state = self.prev_state