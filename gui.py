import pygame
from pygame import Vector2, Surface


class Element():
    """Parent class of all UI elements."""
    
    def __init__(self) -> None:
        self.pos : Vector2
    

    def draw(self, surface : Surface):
        pass


class Label(Surface):
    """Draws text to the screen."""

    def __init__ (self, pos, text, font_size=20, font_color=[255,255,255]):
        super().__init__((1, 1))
        self.pos = pos
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.font = pygame.font.SysFont(None, self.font_size)
        self.draw()


    def draw(self):
        text_surface = self.font.render(self.text, True, self.font_color)
        self.fill((0, 0, 0))
        self.blit(text_surface, (0, 0))
        self.set_size(text_surface.get_size())


    def draw(self, text):
        self.text = text
        self.draw_label()


class Container(Surface):
    """Helps layout UI elements inside itself."""

    instances = []

    def __init__(self, pos, size, bg_color=(255, 255, 255)):
        super().__init__(size)
        self.pos = pos
        self.bg_color = bg_color
        self.rect = pygame.Rect(pos, size)
        self.elements = []
        
        self.moving = False
        self.mouse_offset = Vector2(0, 0)

        Container.instances.append(self)

    def draw(self, surface : Surface):
        self.fill(self.bg_color)

        for element in self.elements:
            self.blit(element, element.pos)

        surface.blit(self, self.rect.topleft)


    def add_element(self, element):
        self.elements.append(element)


    def remove_element(self, element):
        self.elements.remove(element)
    
    
    def drag(self, event : pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is clicked inside the container
            if self.rect.collidepoint(event.pos):
                self.moving = True
                self.mouse_offset.x = event.pos[0] - self.rect.x
                self.mouse_offset.y = event.pos[1] - self.rect.y
        elif event.type == pygame.MOUSEBUTTONUP:
            self.moving = False
        elif event.type == pygame.MOUSEMOTION:
            if self.moving:
                # move the container with the mouse
                self.rect.x = event.pos[0] - self.mouse_offset.x
                self.rect.y = event.pos[1] - self.mouse_offset.y