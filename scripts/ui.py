import pygame

class Button():
    def __init__(self, x, y, text, font, color_base, color_hover):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.color_base = color_base
        self.color_hover = color_hover
        
        # Render text and get dimensions
        self.surf = self.font.render(text, True, color_base)
        self.rect = self.surf.get_rect(center=(x, y))
        self.is_hovered = False

    def update(self, mouse_pos):
        """Met a jour le boutton en mode hover"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def draw(self, screen):
        """Dessine le bouton"""
        color = self.color_hover if self.is_hovered else self.color_base
        
        # Re-render si la couleur change
        text_surf = self.font.render(self.text, True, color)
        screen.blit(text_surf, self.rect)

    def is_clicked(self, event):
        """Retourn True si clicke"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                return True
        return False
    
class ImgButton():
    def __init__(self, x, y, color_base, color_hover, image_surface,is_selected = False):
        self.x = x
        self.y = y
        self.color_base = color_base
        self.color_hover = color_hover
        self.image_surface = image_surface
        self.rect = image_surface.get_rect(center = (x,y))
        self.is_selected = False
        # Render text and get dimensions
        self.rect = image_surface.get_rect(center=(x, y))
        self.is_hovered = False

    def update(self, mouse_pos):
        """Met a jour le boutton en mode hover"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def outline(self,screen,is_selected):
        if is_selected:
            outline_rect = self.rect.inflate(10, 10) 
            pygame.draw.rect(screen, (0, 255, 0), outline_rect, width=10)
            

    def draw(self, screen):
        """Dessine le bouton"""
        # color = self.color_hover if self.is_hovered else self.color_base

        if self.is_hovered:
            contour_rect = self.rect.inflate(10, 10)
            pygame.draw.rect(screen, (255, 255,0), contour_rect, width=8, border_radius=5)
        else:
            pygame.draw.rect(screen, (240,230,140), self.rect, 6)
        # Re-render si la couleur change
        screen.blit(self.image_surface, self.rect)

    def is_clicked(self, event):
        """Retourn True si clicke"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered:
                return True
        return False
    