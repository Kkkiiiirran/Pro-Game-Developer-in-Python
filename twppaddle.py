import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

ball_img = pygame.image.load("table-tennis-ball-clipart (1).png")
ball_img = pygame.transform.scale(ball_img, (50, 50))

class Paddle:
    def __init__(self, x, y, color, start_lives=3):
        self.width = 100
        self.height = 20
        self.x = x
        self.y = y
        self.speed = 5
        self.color = color

        # Score system
        self.lives = start_lives
        self.score = 0

    def move(self, left_pressed, right_pressed):
        if left_pressed:
            self.x -= self.speed
            if self.x < 0:
                self.x = 0
        if right_pressed:
            self.x += self.speed
            if self.x > WIDTH - self.width:
                self.x = WIDTH - self.width

    def hit(self):
        """Called when ball hits this paddle."""
        self.score += 1

    def miss(self):
        """Called when ball goes past this paddle."""
        self.lives -= 1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.get_rect())

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Ball:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.reset()

    def reset(self):
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT // 2 - self.height // 2
        self.dx = 3
        self.dy = 3

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # bounce off side walls
        if self.x <= 0 or self.x >= WIDTH - self.width:
            self.dx *= -1

    def bounce_if_hit_paddle(self, paddle):
        ball_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if ball_rect.colliderect(paddle.get_rect()):
            self.dy *= -1
            paddle.hit()  # tell the paddle it hit the ball

    def draw(self, surface):
        surface.blit(ball_img, (self.x, self.y))


# Create two paddles
paddle1 = Paddle(200, 420, (255, 255, 0))  # bottom player
paddle2 = Paddle(200, 60, (0, 255, 255))   # top player
ball = Ball()

# Key states
p1_keys = [False, False]  # [LEFT, RIGHT]
p2_keys = [False, False]  # [A, D]

font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p1_keys[0] = True
            if event.key == pygame.K_RIGHT:
                p1_keys[1] = True
            if event.key == pygame.K_a:
                p2_keys[0] = True
            if event.key == pygame.K_d:
                p2_keys[1] = True

        # Key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p1_keys[0] = False
            if event.key == pygame.K_RIGHT:
                p1_keys[1] = False
            if event.key == pygame.K_a:
                p2_keys[0] = False
            if event.key == pygame.K_d:
                p2_keys[1] = False

    # Move paddles
    paddle1.move(p1_keys[0], p1_keys[1])
    paddle2.move(p2_keys[0], p2_keys[1])

    # Move ball
    ball.move()
    ball.bounce_if_hit_paddle(paddle1)
    ball.bounce_if_hit_paddle(paddle2)

    # Check misses
    if ball.y > HEIGHT:  # ball passed bottom
        paddle1.miss()
        ball.reset()
    if ball.y < -ball.height:  # ball passed top
        paddle2.miss()
        ball.reset()

    # Draw objects
    paddle1.draw(screen)
    paddle2.draw(screen)
    ball.draw(screen)

    # Draw HUD
    p1_text = font.render(f"P1 Score: {paddle1.score}  Lives: {paddle1.lives}", True, (255, 255, 255))
    p2_text = font.render(f"P2 Score: {paddle2.score}  Lives: {paddle2.lives}", True, (255, 255, 255))
    screen.blit(p1_text, (10, 10))
    screen.blit(p2_text, (10, 40))

    # Check game over
    if paddle1.lives <= 0 or paddle2.lives <= 0:
        game_over_text = font.render("Game Over! Press ESC to quit.", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        clock.tick(10)
        continue

    pygame.display.update()
    clock.tick(60)

pygame.quit()
