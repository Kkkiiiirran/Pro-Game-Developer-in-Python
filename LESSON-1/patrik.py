import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))

running = True

class John:
    def __init__(self,color, w, h, x, y):
        self.color= color
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.dimensions = (self.x, self.y,  self.width, self.height)
  
    def drawrectangle(self):
        pygame.draw.rect(screen, self.color, self.dimensions)



rectangle1= John('green',100, 200, 100, 50)
rectangle2= John('hot pink', 200, 100, 300, 50)
while running:
     rectangle1.drawrectangle() 
     rectangle2.drawrectangle() 
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
             break
     pygame.display.update()