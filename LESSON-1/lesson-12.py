
import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Rect():
    def __init__(self, color, dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = dimensions
    
    def draw(self):
        pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

greenRect = Rect(green, (0,0, 100, 100))
redRect = Rect(red, (200, 200, 150, 150))
blueRect = Rect(blue, (400, 400, 200, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill(white)
    greenRect.draw()
    redRect.draw()
    blueRect.draw()
    pygame.display.update()


pygame.quit()