import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

class Spaceship:
    def __init__(self, imageurl, angle, pos):
        self.image  = pygame.image.load(imageurl)
        self.image  = pygame.transform.scale(self.image,(75,75))
        self.image  = pygame.transform.rotate(self.image,angle)
        self.rect   = self.image.get_rect(center = pos)


bg = pygame.image.load('twoplayer_game\space.png')
bg = pygame.transform.scale(bg,(800,600))

red_ship= Spaceship('twoplayer_game\spaceship_red.png', +90, (100,300))
yellow_ship= Spaceship('twoplayer_game\spaceship_yellow.png', -90,(700,300))



running = True

while running:
    screen.blit(bg, (0,0))
    screen.blit(red_ship.image,red_ship.rect.topleft)
    screen.blit(yellow_ship.image,yellow_ship.rect.topleft)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
            break
    pygame.display.update()                                                                                                                                          
                                                                           