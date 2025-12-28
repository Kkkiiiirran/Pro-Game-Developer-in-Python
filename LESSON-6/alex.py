
import pygame
pygame.init()



class Spaceship:

    def __init__(self, imageurl, x, y, angle):
        self.image = pygame.image.load(imageurl)
        self.image= pygame.transform.scale(self.image, (80,80))
        self.image = pygame.transform.rotate(self.image, angle)
        self.x = x 
        self.y = y
        
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y) )
    



screen= pygame.display.set_mode((1000,600))

bg = pygame.image.load("LESSON-6\Assets\space.png")
bg = pygame.transform.scale(bg, (1000,600))

red_ship = Spaceship("LESSON-6/Assets/spaceship_red.png", 200,200, 90)
yellow_ship = Spaceship("LESSON-6/Assets/spaceship_yellow.png", 700,200, -90)

running=True
while running:
    screen.blit(bg,(0,0))
    red_ship.draw()
    yellow_ship.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            break
    
    pygame.display.update()
                                            