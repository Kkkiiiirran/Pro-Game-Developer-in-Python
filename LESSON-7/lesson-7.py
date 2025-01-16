import pygame

class GameDisplay:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption("Game Selector")
        self.font = pygame.font.SysFont("Times New Roman", 36)
        self.running = True
        self.images = {}
        self.positions = {}

    def load_images(self):
        """Loads images for display."""
        self.images = {
            "subway_surfer": pygame.image.load("LESSON-7/subwaysurfer.png"),
            "ludo": pygame.image.load("LESSON-7/ludo.png"),
            "templerun": pygame.image.load("LESSON-7/templerun.png"),
            "candycrush": pygame.image.load("LESSON-7/candycrush.jpg"),
        }

        self.positions = {
            "subway_surfer": (150, 100),
            "ludo": (150, 200),
            "templerun": (150, 300),
            "candycrush": (150, 400),
        }

    def draw_images_and_text(self):
        """Draws images and associated text on the screen."""
        for key, pos in self.positions.items():
            self.screen.blit(self.images[key], pos)

        texts = {
            "Subway Surfer": (350, 200),
            "Temple Run": (350, 400),
            "Ludo": (350, 100),
            "Candy Crush": (350, 300),
        }

        for text, pos in texts.items():
            rendered_text = self.font.render(text, True, (0, 0, 0))
            self.screen.blit(rendered_text, pos)

        pygame.display.update()

    def draw_shapes_on_mouse_events(self):
        """Handles mouse events for drawing shapes."""
        pos = None  # Store the starting position of the mouse
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    pygame.draw.circle(self.screen, (255, 0, 0), pos, 10, 0)
                    pygame.display.update()

                elif event.type == pygame.MOUSEBUTTONUP and pos:
                    pos2 = pygame.mouse.get_pos()
                    pygame.draw.line(self.screen, (255, 0, 0), pos, pos2, 5)
                    pygame.draw.circle(self.screen, (255, 0, 0), pos2, 10, 0)
                    pygame.display.update()

        pygame.quit()

    def run(self):
        """Main loop to set up and run the game display."""
        self.load_images()
        self.draw_images_and_text()
        self.draw_shapes_on_mouse_events()


if __name__ == "__main__":
    game_display = GameDisplay(600, 600)
    game_display.run()
