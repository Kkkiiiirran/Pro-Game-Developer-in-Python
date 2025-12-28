import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))

running = True


class John:
    def __init__(self,color,w , h , x , y):
        self.color= color
        self.width= w
        self.height= h
        self.x= x
        self.y= y
        self.dimensions= (self.x , self.y, self.width, self.height)

    
    def drawrectangle(self):
        pygame.draw.rect(screen,self.color,self.dimensions)


    def growshape(self):
        self.width+=20
        self.height+=20
        self.dimensions = (self.x , self.y, self.width, self.height)


rectangle1= John('green',30,30,60,200)
rectangle2= John( 'red', 30,30,120,357)

while running:
     rectangle1.drawrectangle()
     rectangle2.drawrectangle()
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.MOUSEBUTTONDOWN:
             rectangle1.growshape()
             
             break
     pygame.display.update()