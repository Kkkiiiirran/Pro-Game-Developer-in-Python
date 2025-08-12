import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()


class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 20
        self.x = 200
        self.y = 420
        self.speed = 5

    def move(self, keys):
        if keys[0]:  # LEFT
            self.x -= self.speed
            if self.x < 0:
                self.x = 0
        if keys[1]:  # RIGHT
            self.x += self.speed
            if self.x > 500 - self.width:
                self.x = 500 - self.width

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 0), self.get_rect())

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Ball:
    def __init__(self):
        self.radius = 25
        self.x = 100
        self.y = 100
        self.dx = 3
        self.dy = 3

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius <= 0 or self.x + self.radius >= 500:
            self.dx *= -1
        if self.y - self.radius <= 0:
            self.dy *= -1
        if self.y + self.radius >= 500:
            self.dy *= -1

    def bounce_if_hit_paddle(self, paddle_rect):
        ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                self.radius * 2, self.radius * 2)
        if ball_rect.colliderect(paddle_rect) and self.dy > 0:
            self.dy *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 255, 255), (self.x, self.y), self.radius)


# Main Game Logic
paddle = Paddle()
ball = Ball()

# Track key state: [LEFT, RIGHT]
keys = [False, False]

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[0] = True
            if event.key == pygame.K_RIGHT:
                keys[1] = True

        # Key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0] = False
            if event.key == pygame.K_RIGHT:
                keys[1] = False

    # Game object updates
    paddle.move(keys)
    ball.move()
    ball.bounce_if_hit_paddle(paddle.get_rect())

    # Draw everything
    paddle.draw(screen)
    ball.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
