import random
import pygame 
pygame.init()


class Circle:
    def __init__(self, rad, pos, color):
        self.radius = rad
        self.center = pos
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, self.center, self.radius)
    
    def grow(self):
        if self.check_click():
            self.radius+=10
    
    def change_color(self):
        if self.check_click():
            r = random.randint(0,255)
            g = random.randint(0,255)
            b= random.randint(0,255)
            self.color = (r,g,b)
    
    def check_click(self):
        x,y = pygame.mouse.get_pos()
        centerx, centery = self.center
        if (centerx-self.radius<=x<=centerx+self.radius) and (centery-self.radius<=y<=centery+self.radius):
            return True 
        else:
            return False


screen  = pygame.display.set_mode((500,500))

running = True 

circle1 = Circle(50, (100,200), "white")
circle2 = Circle(100, (300,200), "pink")

while running:
    screen.fill('blue')
    circle1.draw()
    circle2.draw()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            break
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle1.grow()
            circle2.grow()
            circle1.change_color()
            circle2.change_color()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     rad+=10
            


    pygame.display.update()