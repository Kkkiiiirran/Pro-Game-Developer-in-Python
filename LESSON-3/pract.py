import pygame

pygame.init()

screen = pygame.display.set_mode([500,500])
screen.fill((255,255,255))
running = True

class Circle():
    def __init__(self, color, pos,rad, wid=0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn = screen

    def draw(self):
        pygame.draw.circle(self.scrn,self.color, self.pos, self.rad, self.wid)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        else:
            # pygame.draw.circle(screen, (255,20,40), (50,50), 40)
            pygame.display.update() 
pygame.quit()