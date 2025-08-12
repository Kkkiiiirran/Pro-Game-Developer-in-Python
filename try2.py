import pygame
import random
pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((122,255,122))
bee = pygame.image.load("bee.png")
flower = pygame.image.load("flower.png")
x = 100
y = 100
fx = random.randint(0,WIDTH)
fy = random.randint(0,HEIGHT)
moving = True
move = [0,10]

bee_width, bee_height = bee.get_width(), bee.get_height()
flower_width, flower_height = flower.get_width(), flower.get_height()

while True:
    
    screen.fill((122,255,122))
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving = False
                move[0] = 10
                move[1] = 0
            elif event.key == pygame.K_LEFT:
                moving = False
                move[0] = -10
                move[1] = 0
            elif event.key == pygame.K_UP:
                moving = False
                move[0] = 0
                move[1] = -10
            elif event.key == pygame.K_DOWN:
                moving = False
                move[0] = 0
                move[1] = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving = True
            elif event.key == pygame.K_LEFT:
                moving = True
            elif event.key == pygame.K_UP:
                moving = True
            elif event.key == pygame.K_DOWN:
                moving = True
     
        bee_rect = pygame.Rect(x, y, bee_width, bee_height)
        flower_rect = pygame.Rect(fx, fy, flower_width, flower_height)      
        if not moving:
            x+=move[0]
            y+=move[1]
        if bee_rect.colliderect(flower_rect):
            fx = random.randint(0, WIDTH - flower_width)
            fy = random.randint(0, HEIGHT - flower_height)
        
        screen.blit(bee,(x,y))
        screen.blit(flower,(fx,fy))
        pygame.display.update()

        
        
    

            
        