#importing library
import pygame
#initilize pygame
pygame.init()
#create screen
screen = pygame.display.set_mode((500,500))
screen.fill((0,0,0))
#Inital image is off
image=pygame.image.load("LESSON-4\BulbOn.png")
pygame.display.update()
#mouse down to ON(Click on screen)
# mouse up(release)to OFF
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        image=pygame.image.load("LESSON-4\BulbOn.png")
        screen.fill((255,255,255))
        screen.blit(image,(0,0))
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        # image=pygame.image.load("LESSON-4\BulbOn.png")
        # screen.blit(image,(0,0))
        screen.fill((0,0,0))
        pygame.display.update()