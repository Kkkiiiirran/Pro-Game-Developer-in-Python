import pygame
import random

pygame.init()

screen = pygame.display.set_mode([500, 500])
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

screen.fill(white)

class Rectangle():
    def __init__(self, color, pos, width, height):
        self.color = color
        self.pos = pos
        self.width = width
        self.height = height
        self.scrn = screen
    
    def draw(self):
        pygame.draw.rect(self.scrn, self.color, pygame.Rect(self.pos, (self.width, self.height)))
    
    def grow(self, x, y):
        self.width += x
        self.height += y
        self.draw()
    
    def change_color(self):
   
        color_list = [red, green, blue, yellow]
        self.color = random.choice(color_list)
        self.draw()


position = (150, 150)
width = 100
height = 60
rect = Rectangle(blue, position, width, height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
         
            rect.change_color()
            rect.grow(10, 10)  
            pygame.display.update()
        
    pygame.display.update()

pygame.quit()
