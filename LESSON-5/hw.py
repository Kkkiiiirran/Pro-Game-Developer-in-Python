import time
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])

player = pygame.image.load("LESSON-5/character.png")
background = pygame.image.load("LESSON-5/background.png")

player_x = 200
player_y = 200

goal_x = 500
goal_y = 200
goal_reached = False

keys = [False, False, False, False]
running = True
start_time = time.time()

while running:
    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, player_y))

    elapsed_time = time.time() - start_time
    time_limit = 15

    if not goal_reached and player_x >= goal_x - 50 and player_y >= goal_y - 50 and player_y <= goal_y + 50:
        goal_reached = True
        print("You win!")
        pygame.display.update()
        time.sleep(2)
        break

    if elapsed_time >= time_limit and not goal_reached:
        print("You lose! Time's up!")
        pygame.display.update()
        time.sleep(2)
        break

    remaining_time = max(0, time_limit - elapsed_time)
    font = pygame.font.SysFont(None, 36)
    time_text = font.render(f"Time Left: {int(remaining_time)}s", True, (255, 255, 255))
    screen.blit(time_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_DOWN:
                keys[1] = True
            elif event.key == pygame.K_LEFT:
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_DOWN:
                keys[1] = False
            elif event.key == pygame.K_LEFT:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False

    if keys[0]:
        if player_y > 0:
            player_y -= 7
    elif keys[1]:
        if player_y < 536:
            player_y += 7

    if keys[2]:
        if player_x > 0:
            player_x -= 2

    elif keys[3]:
        if player_x < 536:
            player_x += 2

    player_y += 5
    time.sleep(0.05)
    pygame.display.flip()

pygame.quit()
