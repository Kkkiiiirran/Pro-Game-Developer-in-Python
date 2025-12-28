import pygame
import random

circs = []

k = False

class Circle:
    def __init__(self, g, c, colo):
        self.radius = g
        self.center = c
        self.color = colo
    def draw(self):
        pygame.draw.circle(surface = screen, color=self.color, center = self.center, radius = self.radius)
    def cullur(self):
        r = random.randint(0,255)
        h = random.randint(0,255)
        b = random.randint(0,255)
        self.color = (r,h,b)
    def gro(self):
        cx, cy = self.center
        x, y = pygame.mouse.get_pos()
        if (x >= cx - self.radius and x <= cx + self.radius) and (y >= cy - self.radius and y <= cy + self.radius):
            self.radius += 1
            self.cullur()

def mak():
        # if k == True:
            r = random.randint(0,255)
            h = random.randint(0,255)
            b = random.randint(0,255)
            circ = Circle(random.randint(1,10), (random.randint(5,695),random.randint(5,695)), (r,h,b))
            circs.append(circ)

pygame.init()

screen = pygame.display.set_mode((700,700))

c1 = Circle(6, (350,350), "green")
c2 = Circle(7, (125,125), "yellow")

running = True
while running:
    screen.fill("blue")
    c1.draw()
    c2.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        # if event.type == pygame.MOUSEBUTTONDOWN:
           
        if event.type == pygame.MOUSEMOTION:
            mak()
        # if event.type == pygame.KSCAN_A:
        #     if k == False:
        #         k = True
        #     elif k == True:
        #         k = False
    for i in range(len(circs)):
        circs[i].draw()
    pygame.display.update()