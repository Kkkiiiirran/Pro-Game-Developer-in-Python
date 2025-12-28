
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500,500))

rocket = pygame.image.load("LESSON-5/character.png")
bg = pygame.image.load("LESSON-5/background.png")
running=True

x,y = 100,100
KEYS = [False, False, False, False]
while running:
    screen.blit(bg, (0,0))
    screen.blit(rocket, (x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False 
            break
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                KEYS[2] = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                KEYS[2] = False
    
   
    if KEYS[2] == True:
        y-=3
        

    time.sleep(0.05)
    pygame.display.update()



pygame.quit()