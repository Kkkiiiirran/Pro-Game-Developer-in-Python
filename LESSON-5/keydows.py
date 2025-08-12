import pygame
import time
pygame.init()

screen = pygame.display.set_mode([500,500])
rocket = pygame.image.load("LESSON-5\character.png")


x,y = 100,100
running = True

keys = [False, False]

while running:
    screen.fill((255,255,255))
    screen.blit(rocket, (x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
            
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys[0] = True
            if event.key == pygame.K_RIGHT:
                keys[1] = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0] = False
            if event.key == pygame.K_LEFT:
                keys[1] = False

    if keys[0]:
        x-=3
    if keys[1]:
        x+=3
    
    time.sleep(0.05)

    
    pygame.display.update()
    

