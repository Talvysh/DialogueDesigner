#more UI classes
import pygame

class Label(pygame.surface):
    def __init__ (self, pos, text, font_size=20, font_color=[255,255,255]):
        super().__init__((1, 1))
        self.pos = pos
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.font = pygame.font.SysFont(None, self.font_size)
        self.draw_label()
        
    def draw_label(self):
        text_surface = self.font.render(self.text, True, self.font_color)
        self.fill((0, 0, 0))
        self.blit(text_surface, (0, 0))
        self.set_size(text_surface.get_size())

    def set_text(self, text):
        self.text = text
        self.draw_label()
        
pygame.init()
        