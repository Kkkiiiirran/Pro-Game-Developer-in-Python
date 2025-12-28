import pygame
pygame.init()



class Circle:
    def __init__(self, color, center, radius):
        self.color = color 
        self.center = center 
        self.radius = radius

    def draw(self):
        pygame.draw.circle(sc, color = self.color, center = self.center, radius=self.radius)
    
    def change_size(self):
        self.radius+=10
    
    # def check_click(self,pos):



cir1 = Circle("red",(100,100), 20)
cir2 = Circle("blue",(200,100), 50)

sc = pygame.display.set_mode((500,500))

running = True

while running:
    cir1.draw()
    cir2.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False 
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos, cir1.center)
            if event.pos[0]>=cir1.center[0]-cir1.radius or  event.pos[0]>=cir1.center[0]+cir1.radius :
                cir1.change_size()




    pygame.display.update()
    
 


