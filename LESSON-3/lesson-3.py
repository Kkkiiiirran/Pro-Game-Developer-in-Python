import pygame
pygame.init()
#global variables
screen = pygame.display.set_mode([500,500])
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white=(255,255,255)
yellow = (255,255,0)
black=(0,0,0)

screen.fill(white)

class myCircle():
    def __init__(self,color, pos, rad, wid=0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn = screen
        
    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid )

    def grow(self,x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid )
        
#how to draw a circle
position = (300,300)
radius = 50
wid = 2
pygame.draw.circle(screen, red, position, radius, wid )
pygame.display.update()

#creating instances
blueCircle = myCircle(blue, position, radius+60)
redCircle = myCircle(red, position, radius+40)
yellowCircle = myCircle(yellow, position, radius, 5)
greenCircle = myCircle(green, position, 20)

running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            blueCircle.grow(2)
            redCircle.grow(2)
            yellowCircle.grow(2)
            greenCircle.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = myCircle(black, pos, 5)
            blackCircle.draw()
            pygame.display.update()
            

        
pygame.quit()