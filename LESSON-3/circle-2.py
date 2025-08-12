import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))


start = True

class Circle():
    def __init__(self,colour,center,radius):
        self.colour = colour
        self.radius = radius
        self.center = center
        self.scrn = screen
    def draw(self):
        pygame.draw.circle(self.scrn,self.colour,self.center,self.radius)
    def grow(self):
        self.radius +=10
        pygame.draw.circle(self.scrn,self.colour,self.center,self.radius)

tiny_circle = Circle((0,0,255),(250,250),20)
radius = 20
while start:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            start = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # tiny_circle = Circle((0,0,255),(250,250),radius)
            # medium_circle = Circle((0,255,0),(250,250),radius+20)
            # big_circle = Circle((255,0,0),(250,250),radius+40)
            
            # big_circle.draw()
            # medium_circle.draw()
            tiny_circle.draw()
        elif event.type == pygame.MOUSEBUTTONUP:
            tiny_circle.grow()
        pygame.display.update()
    # pygame.display.update()