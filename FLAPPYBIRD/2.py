# lesson2.py
import pygame, random, sys

pygame.init()
WIDTH, HEIGHT = 800, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

bg = pygame.image.load("FLAPPYBIRD/bg.png")
ground = pygame.image.load("FLAPPYBIRD/ground.png")

pipegap = 300
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
scroll_speed = 4

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.image.load(f"FLAPPYBIRD/bird{i+1}.png") for i in range(3)]
        self.index, self.image = 0, self.images[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0
        self.alive = True

    def update(self, flying):
        if flying and self.alive:
            self.velocity += 0.5
            if self.velocity > 8: self.velocity = 8
            if self.rect.bottom < 700:
                self.rect.y += self.velocity
            if pygame.mouse.get_pressed()[0]:
                self.velocity = -10

        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]
        self.image = pygame.transform.rotate(self.image, -self.velocity*2)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        super().__init__()
        self.image = pygame.image.load("FLAPPYBIRD/pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:  # top pipe
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - pipegap//2)
        else:  # bottom pipe
            self.rect.topleft = (x, y + pipegap//2)

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0: self.kill()

bird = Bird(100, HEIGHT//2)
bird_group = pygame.sprite.Group(bird)
pipe_group = pygame.sprite.Group()

flying, game_over = False, False

while True:
    clock.tick(FPS)
    screen.blit(bg, (0,0))
    bird_group.draw(screen)
    pipe_group.draw(screen)
    bird_group.update(flying)
    screen.blit(ground, (0, HEIGHT-200))

    if flying and not game_over:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100,100)
            b_pipe = Pipe(WIDTH, HEIGHT//2+pipe_height, -1)
            t_pipe = Pipe(WIDTH, HEIGHT//2+pipe_height, 1)
            pipe_group.add(b_pipe, t_pipe)
            last_pipe = time_now
        pipe_group.update()

        # Collisions
        if pygame.sprite.spritecollide(bird, pipe_group, False) or bird.rect.bottom >= 700:
            game_over = True
            flying = False
            bird.alive = False

    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True

    pygame.display.update()
