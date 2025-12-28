import pygame



class Bird:
    def __init__(self):
        self.idx = 0
        self.image = pygame.image.load(f"FLAPPYBIRD/bird{self.idx+1}.png")
        self.rect = self.image.get_rect(center = (400,350))
    
    def draw(self):
        self.image = pygame.image.load(f"FLAPPYBIRD/bird{self.idx+1}.png")
        self.rect = self.image.get_rect(center = (400,350))
        screen.blit(self.image,self.rect.center)
        self.idx+=1
        self.idx%=3

pygame.init()

screen = pygame.display.set_mode((800,700))

running = True


bg = pygame.image.load("FLAPPYBIRD/bg.png")
bg = pygame.transform.scale(bg, (800,550))
ground =pygame.image.load("FLAPPYBIRD/ground.png")


bird = Bird()

while running:
    screen.blit(bg, (0,0))
    screen.blit(ground,(0,550))
    bird.draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    pygame.display.update()