# lesson3.py (Final Game)
import pygame, random, sys
pygame.init()

WIDTH, HEIGHT = 800, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
FPS = 60

bg = pygame.image.load("FLAPPYBIRD/bg.png")
ground = pygame.image.load("FLAPPYBIRD/ground.png")

pipegap, pipe_frequency = 300, 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
scroll_speed, scroll_ground = 4, 0
score, pass_pipe = 0, False

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.image.load(f"FLAPPYBIRD/bird{i+1}.png") for i in range(3)]
        self.index, self.image = 0, self.images[0]
        self.rect = self.image.get_rect(center=(x,y))
        self.velocity, self.alive = 0, True

    def update(self, flying, game_over):
        if flying and self.alive:
            self.velocity += 0.5
            if self.velocity > 8: self.velocity = 8
            if self.rect.bottom < 700:
                self.rect.y += self.velocity
            if not game_over and pygame.mouse.get_pressed()[0]:
                self.velocity = -10

        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]
        self.image = pygame.transform.rotate(self.image, -self.velocity*2)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        super().__init__()
        self.image = pygame.image.load("FLAPPYBIRD/pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - pipegap//2)
        else:
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
    bird_group.update(flying, game_over)
    screen.blit(ground, (scroll_ground, HEIGHT-200))

    if flying and not game_over:
        scroll_ground -= scroll_speed
        if scroll_ground <= -35: scroll_ground = 0

        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100,100)
            pipe_group.add(Pipe(WIDTH, HEIGHT//2+pipe_height, -1),
                           Pipe(WIDTH, HEIGHT//2+pipe_height, 1))
            last_pipe = time_now
        pipe_group.update()

        # Score logic
        for pipe in pipe_group:
            if pipe.rect.right < bird.rect.left and not pass_pipe:
                score += 1
                pass_pipe = True
        if pass_pipe and all(p.rect.right < 0 for p in pipe_group):
            pass_pipe = False

        # Collision
        if pygame.sprite.spritecollide(bird, pipe_group, False) or bird.rect.bottom >= 700:
            game_over = True
            flying = False
            bird.alive = False

    # Restart
    if game_over and pygame.mouse.get_pressed()[0]:
        game_over, flying, score, pass_pipe = False, False, 0, False
        pipe_group.empty()
        bird.rect.center, bird.velocity, bird.alive = (100, HEIGHT//2), 0, True

    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True

    pygame.display.set_caption(f"Flappy Bird | Score: {score}")
    pygame.display.update()
