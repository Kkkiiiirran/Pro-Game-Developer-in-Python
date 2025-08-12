import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rect Class Example")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

x = 260
move = [False, False]  # [move_left, move_right]

clock = pygame.time.Clock()


velx = 1
vely = -1

ballx= 50
bally = 60

running = True
while running:
    screen.fill(WHITE)

    # Draw the rect
    my_rect = pygame.Rect(x, 350, 120, 20)
    pygame.draw.rect(screen, GREEN, my_rect)
    pygame.draw.circle(screen, "red", (ballx,bally), 15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move[0] = True
            if event.key == pygame.K_RIGHT:
                move[1] = True
        
        # Key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move[0] = False
            if event.key == pygame.K_RIGHT:
                move[1] = False

    # Update x based on movement
    if move[0]:
        x -= 5
    if move[1]:
        x += 5
    ballx+=velx*3
    bally+=velx*3

    


    # Keep rect within screen bounds
    x = max(0, min(WIDTH - 80, x))

    pygame.display.flip()
    clock.tick(60)  # 60 frames per second

pygame.quit()
sys.exit()
