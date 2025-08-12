import pygame
class GameSetup:
    WIDTH, HEIGHT = 900, 500
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("OOP Space Game")

        self.health_font = pygame.font.SysFont('comicsans', 40)
        self.winner_font = pygame.font.SysFont('comicsans', 100)
        self.border = pygame.Rect(self.WIDTH // 2 - 5, 0, 10, self.HEIGHT)
        self.bg = pygame.transform.scale(pygame.image.load("LESSON-6\Assets\space.png"), (self.WIDTH, self.HEIGHT))

    def draw_window(self, red, yellow, bullet_mgr):
        self.win.blit(self.bg, (0, 0))
        pygame.draw.rect(self.win, self.BLACK, self.border)

        red_health = self.health_font.render(f"Health: {red.health}", 1, self.WHITE)
        yellow_health = self.health_font.render(f"Health: {yellow.health}", 1, self.WHITE)

        self.win.blit(red_health, (self.WIDTH - red_health.get_width() - 10, 10))
        self.win.blit(yellow_health, (10, 10))

        red.draw(self.win)
        yellow.draw(self.win)
        bullet_mgr.draw(self.win)

        pygame.display.update()

    def draw_winner(self, text):
        draw_text = self.winner_font.render(text, 1, self.WHITE)
        self.win.blit(draw_text, (self.WIDTH/2 - draw_text.get_width()/2, self.HEIGHT/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(5000)
