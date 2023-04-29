import pygame


class Button():
    instances = []

    def __init__(self, pos : pygame.Vector2, size : pygame.Vector2) -> None:
        self.position = pygame.Vector2
        self.fill_color = None
        self.outline_color = None
        self.outline_size : float
        self.image : pygame.image
        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
    
        Button.instances.append(self)


    def set_style(self, fill_color, outline_color, outline_size):
        self.fill_color = fill_color
        self.outline_color = outline_color
        self.outline_size = outline_size


    def draw(self, surface : pygame.surface) -> None:
        pygame.draw.rect(surface, self.fill_color, self.rect, 0)

        if self.outline_size > 0:
            pygame.draw.rect(surface, self.outline_color, self.rect, self.outline_size)
        