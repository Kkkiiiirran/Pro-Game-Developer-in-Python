import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 900, 700
GRID_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

# Clock
clock = pygame.time.Clock()

# Load images
pacman_image = pygame.image.load('pacman.png').convert_alpha()
pacman_image = pygame.transform.scale(pacman_image, (GRID_SIZE, GRID_SIZE))

ghost_images = {
    "blinky": pygame.image.load('blinky.png').convert_alpha(),
    "pinky": pygame.image.load('pinky.png').convert_alpha(),
    "inky": pygame.image.load('inky.png').convert_alpha(),
    "clyde": pygame.image.load('clyde.png').convert_alpha(),
}
for key in ghost_images:
    ghost_images[key] = pygame.transform.scale(ghost_images[key], (GRID_SIZE, GRID_SIZE))

fruit_image = pygame.image.load('fruit.png').convert_alpha()
fruit_image = pygame.transform.scale(fruit_image, (GRID_SIZE, GRID_SIZE))

# Classes
class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pacman_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH // 2, HEIGHT // 2)
        self.speed = GRID_SIZE // 2

    def update(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.image = ghost_images[name]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.name = name
        self.speed = GRID_SIZE // 4

    def update(self):
        self.rect.x += random.choice([-self.speed, self.speed])
        self.rect.y += random.choice([-self.speed, self.speed])

class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = fruit_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Groups
all_sprites = pygame.sprite.Group()
ghosts = pygame.sprite.Group()
fruits = pygame.sprite.Group()

# Create Pacman
pacman = Pacman()
all_sprites.add(pacman)

# Create Ghosts
ghost_positions = [(100, 100), (200, 100), (300, 100), (400, 100)]
ghost_names = ["blinky", "pinky", "inky", "clyde"]
for pos, name in zip(ghost_positions, ghost_names):
    ghost = Ghost(*pos, name)
    ghosts.add(ghost)
    all_sprites.add(ghost)

# Create Fruits
for _ in range(10):
    x = random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE
    y = random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE
    fruit = Fruit(x, y)
    fruits.add(fruit)
    all_sprites.add(fruit)

# Game Loop
running = True
score = 0
font = pygame.font.SysFont("Arial", 24)

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    pacman.update(keys)

    # Ghost movement
    ghosts.update()

    # Collision detection
    fruit_collisions = pygame.sprite.spritecollide(pacman, fruits, True)
    for fruit in fruit_collisions:
        score += 10

    ghost_collisions = pygame.sprite.spritecollide(pacman, ghosts, False)
    if ghost_collisions:
        running = False  # End game if Pacman collides with a ghost

    # Draw everything
    all_sprites.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
