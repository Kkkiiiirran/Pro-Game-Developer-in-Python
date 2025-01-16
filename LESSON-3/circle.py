import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white=(255,255,255)
yellow = (255,255,0)
black=(0,0,0)

screen.fill(white)

class Circle():
    def __init__(self, color, pos, rad, wid=0):
        self.color = color
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn = screen
    
    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

    def grow(self,x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid )
position = (300,300)
radius = 50
wid = 2
blueCircle = Circle(blue, position, radius+60)
redCircle = Circle(red, position, radius+40)
yellowCircle = Circle(yellow, position, radius)
greenCircle = Circle(green, position,20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
    
        
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = Circle(black, pos, 2)
            blackCircle.draw()
            pygame.display.update()



pygame.quit()