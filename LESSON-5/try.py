import pygame
import time

pygame.init()

screen = pygame.display.set_mode([600,600])

bg = pygame.image.load("LESSON-5/background.png")
player = pygame.image.load("LESSON-5/character.png")

player_y = 50
player_x = 50

keys = [False, False, False, False]

start = True


while start:
    screen.blit(bg, (0,0))
    screen.blit(player, (player_x,player_y))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                keys[0] = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                keys[0] = False

    if keys[0]:
        player_y-=10








    pygame.display.update()
    time.sleep(0.05)
