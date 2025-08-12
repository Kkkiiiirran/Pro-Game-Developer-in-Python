import time
import pygame

pygame.init()
screen = pygame.display.set_mode([600,600])

player = pygame.image.load("Pro Game Developer in Python\LESSON-5\character.png")
background = pygame.image.load("Pro Game Developer in Python\LESSON-5/background.png")

player_x = 200
player_y = 200

keys = [False, False, False, False]
running = True
while running:
    screen.blit(background, (0,0))
    screen.blit(player, (player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
        
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_DOWN:
                keys[1] = True
            elif event.key == pygame.K_LEFT:
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                keys[3] = True
        
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_DOWN:
                keys[1] = False
            elif event.key == pygame.K_LEFT:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False
    
    if keys[0]:
        if player_y>0:
            player_y-=7
    elif keys[1]:
        if player_y < 536:
            player_y+=7
    
    if keys[2]:
        if player_x>0:
            player_x-=2
    
    elif keys[3]:
        if player_x<536:
            player_x+=2
    

    player_y+=5
    time.sleep(0.05)


            