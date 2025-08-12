import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))

pygame.draw.rect(screen,(0,0,0), (0,0,100,100))

running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    if not running: break

    pygame.draw.rect(screen,(255,0,0), (0,0,100,100))
    pygame.display.update()