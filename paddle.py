import pygame
import sys
import random

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10
FPS = 60

# Paddle Class
class Paddle:
    SPEED = 7

    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.SPEED

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect)


# Ball Class
class Ball:
    SPEED = 5

    def __init__(self):
        self.reset()

    def move(self):
        self.rect.y += self.SPEED

    def reset(self):
        x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
        self.rect = pygame.Rect(x, 0, BALL_RADIUS * 2, BALL_RADIUS * 2)

    def draw(self, win):
        pygame.draw.ellipse(win, WHITE, self.rect)


# Game Class
class Game:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Catch the Falling Ball")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsans", 30)

        self.paddle = Paddle()
        self.ball = Ball()
        self.lives = 3
        self.score = 0

    def draw(self):
        self.win.fill(BLACK)
        self.paddle.draw(self.win)
        self.ball.draw(self.win)

        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)

        self.win.blit(lives_text, (10, 10))
        self.win.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
        pygame.display.update()

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.paddle.move(keys)
            self.ball.move()

            # Check collision
            if self.ball.rect.colliderect(self.paddle.rect):
                self.score += 1
                self.ball.reset()

            # Ball missed
            if self.ball.rect.top > HEIGHT:
                self.lives -= 1
                self.ball.reset()

            self.draw()

            if self.lives <= 0:
                self.game_over()
                running = False

        pygame.quit()
        sys.exit()

    def game_over(self):
        msg = self.font.render("Game Over! Press any key to exit.", True, WHITE)
        self.win.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))
        pygame.display.update()
        pygame.time.delay(1000)

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    waiting = False


if __name__ == "__main__":
    Game().run()
