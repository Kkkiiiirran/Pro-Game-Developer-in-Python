# lesson1.py
import pygame, sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird - Lesson 1")
clock = pygame.time.Clock()
FPS = 60

# Load images
bg = pygame.image.load("FLAPPYBIRD/bg.png")
ground = pygame.image.load("FLAPPYBIRD/ground.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.image.load(f"FLAPPYBIRD/bird{i+1}.png") for i in range(3)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0

    def update(self, flying):
        if flying:
            self.velocity += 0.5  # gravity
            if self.velocity > 8: self.velocity = 8
            self.rect.y += self.velocity

            if pygame.mouse.get_pressed()[0]:  # flap on click
                self.velocity = -10

        # animate wings
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]
        self.image = pygame.transform.rotate(self.image, -self.velocity * 2)

# Groups
bird = Bird(100, HEIGHT//2)
bird_group = pygame.sprite.Group(bird)

flying = False
run = True
while run:
    clock.tick(FPS)
    screen.blit(bg, (0,0))

    # Draw bird
    bird_group.draw(screen)
    bird_group.update(flying)
    screen.blit(ground, (0, HEIGHT-200))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            flying = True  # Start game

    pygame.display.update()
