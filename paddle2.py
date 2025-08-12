import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

ball_img = pygame.image.load("table-tennis-ball-clipart (1).png")
ball = pygame.transform.scale(ball_img, (50, 50))

x, y = 200, 420  # Paddle position

# Ball position and velocity
ballx, bally = 100, 100
dx, dy = 3, 3  # Velocity in X and Y

running = True
keys = [False, False]
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[0] = True
            if event.key == pygame.K_RIGHT:
                keys[1] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0] = False
            if event.key == pygame.K_RIGHT:
                keys[1] = False

    if keys[0]:
        x -= 3
        if x < 0:
            x = 0
    if keys[1]:
        x += 3
        if x > 500:
            x = 500

    # Ball movement
    ballx += dx
    bally += dy

    # Bounce off walls
    if ballx <= 0 or ballx >= 500 - 50:
        dx *= -1
    if bally <= 0:
        dy *= -1

    # Paddle collision
    paddle = pygame.Rect(x, y, 100, 20)
    ball_rect = pygame.Rect(ballx, bally, 50, 50)
    if ball_rect.colliderect(paddle) and dy > 0:
        dy *= -1

    # Bottom screen bounce (optional lose condition)
    if bally >= 500 - 50:
        dy *= -1  # or end game / reset

    # Draw paddle and ball
    pygame.draw.rect(screen, (255, 255, 0), paddle)
    screen.blit(ball, (ballx, bally))

    pygame.display.update()
    clock.tick(60)
