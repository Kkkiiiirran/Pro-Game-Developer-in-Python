import pygame
pygame.init()
screen= pygame.display.set_mode((600,600))
screen.fill((255,255,255))
blue = (0,0,255)
pygame.display.update()


class Circle():
    def __init__(self,color,pos,radius,width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius      
        self.circle_width = width
        self.circle_surface = screen
        
    def draw(self):
        self.Draw_Circle = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

    def grow(self,r):
        self.circle_radius+=20 
        # self.Draw_Circle = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

circle=Circle(blue,(300,300),25,0)
running = True

while running:
    circle.draw()
            
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # screen.fill((255,255,255))
            circle.grow(20)
            # circle.draw()
            
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     # screen.fill((255,255,255))
        #     # circle.grow(20)
        #     pygame.display.update()
        pygame.display.update()