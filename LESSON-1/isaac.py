import pygame 
pygame.init()


class Rectangle:
    def __init__(self,color, width, height):
        # self.width = width
        self.width = width
        self.height= height
        self.color = color
        self.rect = ((250,250), (self.width, self.height))

    
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)


screen = pygame.display.set_mode((500,500))
running = True


blue_rect = Rectangle("blue",50, 100)
pink_rect = Rectangle("pink",100, 50)
while running:
    blue_rect.draw()
    pink_rect.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.display.update()
pygame.quit()