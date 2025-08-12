import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))


start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            break
        else:
            pygame.draw.circle(screen, (255,0,0),center = (50,50), radius=40)
        
        pygame.display.update()


