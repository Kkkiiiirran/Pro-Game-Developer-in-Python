import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 500
HEIGHT = 500

# Colors
WHITE = (255, 255, 255)
PINK = (255, 182, 193)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bee Game")

# Load images
bee_image = pygame.image.load('LESSON-6/bee.png')
flower_image = pygame.image.load('LESSON-6/flower.png')
background_image = pygame.image.load('LESSON-6/background.png')

# Classes
class Bee:
    def __init__(self):
        self.image = bee_image
        self.rect = self.image.get_rect(center=(250, 250))

    def draw(self):
        screen.blit(self.image, self.rect)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2

class Flower:
    def __init__(self):
        self.image = flower_image
        self.rect = self.image.get_rect()
        self.place()

    def draw(self):
        screen.blit(self.image, self.rect)

    def place(self):
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = random.randint(100, HEIGHT - 50)

class Game:
    def __init__(self):
        self.bee = Bee()
        self.flower = Flower()
        self.score = 0
        self.game_over = False
        self.font = pygame.font.Font(None, 40)
        self.timer = pygame.time.get_ticks()

    def check_collision(self):
        if self.bee.rect.colliderect(self.flower.rect):
            self.flower.place()
            self.score += 5

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (400, 20))

    def draw_game_over(self):
        screen.fill(PINK)
        game_over_text = self.font.render(f"Time's Up! Your final score is {self.score}", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.game_over:
                # Update game state
                self.bee.move(keys)
                self.check_collision()

                # Check timer
                if (pygame.time.get_ticks() - self.timer) > 60000:  # 60 seconds
                    self.game_over = True

                # Draw everything
                screen.blit(background_image, (0, 0))
                self.bee.draw()
                self.flower.draw()
                self.draw_score()
            else:
                self.draw_game_over()

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

# Run the game
if __name__ == "__main__":
    Game().run()