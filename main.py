import pygame
from button import Button


class App():
    def __init__(self) -> None:
        print("Starting up DD...")
        pygame.init()

        self.window_size = [1280, 720]  # Save to a config later
        self.window = pygame.display.set_mode(self.window_size)
        self.running = True

        self.create_ui()
        self.render()


    def render(self):
        while self.running:
            self.input(self)
            
            self.window.fill([0,0,0])

            for b in Button.instances:
                b.draw(self.window)
            
            pygame.display.flip()
        
        self.quit()

    
    def input(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False


    def create_ui(self):
        button = Button(pygame.Vector2(200, 200), pygame.Vector2(150, 25))
        button.set_style([0, 200, 100], [255, 255, 255], 3)


    def quit(self):
        print("Doing a clean exit...")
        self.running = False
        pygame.quit()
        
        #Testing changes


App()