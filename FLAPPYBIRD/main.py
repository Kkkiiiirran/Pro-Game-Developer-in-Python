import pygame, random

pygame.init()

WIDTH = 800
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
fps = 60
clock = pygame.time.Clock()  # 💬 Added clock to control frame rate

pipegap = 300
pipe_frequency = 1500  # milliseconds

# 💬 FIXED: Typo in get_tics() -> get_ticks()
last_pipe = pygame.time.get_ticks() - pipe_frequency

pass_pipe = False
fly = False
GAME_OVER = False
scroll_ground = 0
scroll_speed = 4
score = 0  # 💬 NEW: Track the player's score

pygame.display.set_caption("drib yppalf")

# Load images
bg = pygame.image.load("FLAPPYBIRD/bg.png")
ground = pygame.image.load("FLAPPYBIRD/ground.png")


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        self.index = 0
        self.counter = 0

        for i in range(3):
            img = pygame.image.load(f"FLAPPYBIRD/bird{i+1}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.alive = True

    def update(self):
        if fly and self.alive:
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 700:
                self.rect.y += self.velocity
        
        if self.alive:
            if not GAME_OVER:
                if pygame.mouse.get_pressed()[0] == 1:
                    self.velocity = -10

            flap_cooldown = 5
            self.counter += 1
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.image, self.velocity * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.image], 90)

        # 💬 NEW: Clamp bird to top of screen
        if self.rect.top < 0:
            self.rect.top = 0


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        super().__init__() #super used
        self.image = pygame.image.load("FLAPPYBIRD/pipe.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipegap / 2)]
        if pos == -1:
            self.rect.topleft = [x, y + int(pipegap / 2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()


# Groups
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
drib = Bird(100, HEIGHT / 2)
bird_group.add(drib)

run = True
while run:
    clock.tick(fps)  # 💬 NEW: Control game loop speed
    screen.blit(bg, (0, 0))
    bird_group.draw(screen)
    pipe_group.draw(screen)
    bird_group.update()
    screen.blit(ground, (scroll_ground, HEIGHT - 200))

    if fly and not GAME_OVER:
        scroll_ground -= scroll_speed
        if scroll_ground < -35:
            scroll_ground = 0

        # 💬 NEW: Pipe generation logic
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            b_pipe = Pipe(WIDTH, HEIGHT / 2 + pipe_height, -1)
            t_pipe = Pipe(WIDTH, HEIGHT / 2 + pipe_height, 1)
            pipe_group.add(b_pipe)
            pipe_group.add(t_pipe)
            last_pipe = time_now

        pipe_group.update()

        # 💬 NEW: Score tracking when bird passes pipes
        for pipe in pipe_group:
            if pipe.rect.right < drib.rect.left and not pass_pipe:
                score += 1
                pass_pipe = True
        if pass_pipe:
            if pipe.rect.right < 0:
                pass_pipe = False

        # 💬 NEW: Collision detection with pipes
        if pygame.sprite.spritecollide(drib, pipe_group, False):
            GAME_OVER = True
            fly = False

    # Ground hit = game over
    if drib.rect.bottom >= 700:
        GAME_OVER = True
        fly = False
        drib.alive = False

    # 💬 NEW: Restart logic after game over
    if GAME_OVER:
        if pygame.mouse.get_pressed()[0]:
            GAME_OVER = False
            fly = False
            score = 0
            pipe_group.empty()
            drib.rect.center = (100, HEIGHT / 2)
            drib.velocity = 0
            drib.alive = True

    # Events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN and not fly and not GAME_OVER:
            fly = True

    # 💬 NEW: Show score in window title
    pygame.display.set_caption(f"drib yppalf | Score: {score}")
    pygame.display.update()

pygame.quit()
