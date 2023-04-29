#UI elements

#Need to add: creation of label, button, container, etc. Then add elements to the container, then add the container to the UI. Then render the UI.

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


#Container class for UI elements:
class Container(pygame.Surface):
    def __init__(self, pos, size, bg_color=(255, 255, 255)):
        super().__init__(size)
        self.pos = pos
        self.bg_color = bg_color
        self.rect = pygame.Rect(pos, size)
        self.elements = []
        self.draw_container()

    def draw_container(self):
        self.fill(self.bg_color)
        for element in self.elements:
            self.blit(element, element.pos)


    def add_element(self, element):
        self.elements.append(element)


    def remove_element(self, element):
        self.elements.remove(element)
    
    
        