import pygame

pygame.init()

class App():
    def __init__(self) -> None:
        print("Starting up DD...")

        self.window_size = [1280, 720]  # Save to a config later
        self.window = pygame.display.set_mode(self.window_size)
        self.running = True

        self.render()


    def render(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

    
    def input(self):
        pass


    def quit(self):
        print("Doing a clean exit...")
        self.running = False
        pygame.quit()


app = App()