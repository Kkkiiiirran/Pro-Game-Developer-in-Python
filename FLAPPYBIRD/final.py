# lesson1.py
import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

# ----------------------------
# Bird Class
# ----------------------------
class Bird:
    def __init__(self, x, y):
        self.images = [pygame.image.load(f"FLAPPYBIRD/bird{i+1}.png") for i in range(3)]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0

    def update(self):
        if not game_over:
            # gravity
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8

            # move vertically
            if self.rect.bottom < 700:
                self.rect.y += self.velocity

            # jump on click
            if pygame.mouse.get_pressed()[0]:
                self.velocity = -10

        # flap animation
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]


# ----------------------------
# Pipe Class
# ----------------------------
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        super().__init__()
        self.image = pygame.image.load("FLAPPYBIRD/pipe.png")
        self.rect = self.image.get_rect()
        self.speed = 4
        pipe_gap = 200

        # Position top or bottom pipe
        if pos == 1:  # top pipe
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - pipe_gap // 2)
        else:  # bottom pipe
            self.rect.topleft = (x, y + pipe_gap // 2)

    def update(self):
        # Move the pipe to the left
        if not game_over:
            self.rect.x -= self.speed
        # Remove pipe if it goes off screen
        if self.rect.right < 0:
            self.kill()


# ----------------------------
# Main Game Setup
# ----------------------------
WIDTH, HEIGHT = 800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

bg = pygame.image.load("FLAPPYBIRD/bg.png")
ground = pygame.image.load("FLAPPYBIRD/ground.png")

bird = Bird(200, 350)
pipe_group = pygame.sprite.Group()

# control pipe spawn timing
pipe_frequency = 1500  # milliseconds
last_pipe_time = pygame.time.get_ticks() - pipe_frequency

# scroll variables
ground_scroll = 0
scroll_speed = 4

# game state
flying = True  # start flying immediately
game_over = False

# ----------------------------
# Main Game Loop
# ----------------------------
while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))

    # ----------------------------
    # PIPE GENERATION
    # ----------------------------
    time_now = pygame.time.get_ticks()
    if flying and not game_over and time_now - last_pipe_time > pipe_frequency:
        pipe_height = random.randint(200, 500)
        b_pipe = Pipe(WIDTH, pipe_height, -1)  # bottom pipe
        t_pipe = Pipe(WIDTH, pipe_height, 1)   # top pipe
        pipe_group.add(b_pipe, t_pipe)
        last_pipe_time = time_now

    # update pipes and bird
    pipe_group.update()
    bird.update()

    # draw everything
    pipe_group.draw(screen)
    screen.blit(bird.image, bird.rect)

    # ----------------------------
    # GROUND SCROLL
    # ----------------------------
    if flying and not game_over:
        ground_scroll -= scroll_speed
        if ground_scroll <= -800:
            ground_scroll = 0
    screen.blit(ground, (ground_scroll, 600))
    screen.blit(ground, (ground_scroll + 800, 600))

    # ----------------------------
    # COLLISION CHECK
    # ----------------------------
    if pygame.sprite.spritecollide(bird, pipe_group, False) or bird.rect.bottom >= 700:
        game_over = True
        flying = False

    # ----------------------------
    # EVENT HANDLING
    # ----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Start flying or restart game on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not flying and not game_over:
                flying = True
            elif game_over:
                # Restart game
                game_over = False
                flying = True
                bird.rect.center = (200, 350)
                bird.velocity = 0
                pipe_group.empty()
                ground_scroll = 0
                last_pipe_time = pygame.time.get_ticks() - pipe_frequency

    pygame.display.update()
