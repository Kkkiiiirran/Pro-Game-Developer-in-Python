import pygame
import random
import os

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join('candy crush', 'bgmusic.mp3'))
pygame.mixer.music.play(-1)  
pygame.mixer.music.set_volume(0.3)

# Window and grid settings
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 6, 6
CELL_SIZE = WIDTH // COLS
FPS = 60

# Path to your candy images folder
CANDY_PATH = os.path.join('candy crush')

# Load candy images
def load_candy_images():
    images = []
    for i in range(1,13):
        path =f"{CANDY_PATH}/{i}.png"
        img = pygame.image.load(path)
        img = pygame.transform.scale(img, (CELL_SIZE - 8, CELL_SIZE - 8))
        images.append(img)
       
    return images

# Candy Sprite class
class Candy(pygame.sprite.Sprite):
    def __init__(self, row, col, candy_type):
        super().__init__()
        self.row = row
        self.col = col
        self.type = candy_type
        img = candy_images[self.type]
      
        self.image = img.copy()

        self.rect = self.image.get_rect()
        self.rect.topleft = (col * CELL_SIZE + 4, row * CELL_SIZE + 4)

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Candy Crush Lesson 1')
clock = pygame.time.Clock()
candy_images = load_candy_images()

# Create candies
sprites = pygame.sprite.Group()
for r in range(ROWS):
    for c in range(COLS):
        candy = Candy(r, c, random.randint(0, 11))
        sprites.add(candy)

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
