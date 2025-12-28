import pygame
import random
pygame.init()
screen = pygame.display.set_mode([600,600])
bg = pygame.image.load("FLAPPYBIRD/bg.png")
ground = pygame.image.load("FLAPPYBIRD/ground.png")
clock = pygame.time.Clock()
class Bird():
    def __init__(self,x,y):
        self.images = [pygame.image.load(f"FLAPPYBIRD/bird{i+1}.png") for i in range(3)]
        self.index = 0
        self.image = self.images[self.index]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.velocity = 0
    def update(self):
        self.index = (self.index+1)%3
        self.image = self.images[self.index]
        self.velocity+=0.2
        self.rect.y+=self.velocity
        # self.rect.x+=2
        
        if pygame.mouse.get_pressed()[0]:
            self.velocity = -5
            # self.rect.y+=self.velocity
 


class Pipe(pygame.sprite.Sprite):
    def __init__(self,invert):
        super().__init__()
        self.image = pygame.image.load("FLAPPYBIRD/pipe.png")
        self.pipe = self.image
        self.rect = self.pipe.get_rect()
        self.y = random.randint(150,300)
        self.x = 600
        self.invert = invert
        self.pipe_gap = 50

        if self.invert == True:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (self.x,self.y-100)
        else:
            
            self.rect.topleft = (self.x,self.y+100)
        
    def update(self):
        self.rect.x -= 10

        if self.rect.x<-20:
            self.kill()
        
        
        #self.rect.topleft = (self.x,random.randint(0,450))

    
bird = Bird(300,300)
pipe_group = pygame.sprite.Group()


prev_time = pygame.time.get_ticks()
print(prev_time)

ground_x = 0
while True:
    clock.tick(70)
    screen.blit(bg,(0,0))
    
    screen.blit(bird.image,(bird.rect))

    
    if pygame.time.get_ticks()-prev_time>1500:
        pipe = Pipe(False)
        pipe2 = Pipe(True)
        pipe_group.add(pipe)
        pipe_group.add(pipe2)
        prev_time =pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    bird.update()
    pipe_group.update()
    pipe_group.draw(screen)
    screen.blit(ground,(ground_x,450))
    screen.blit(ground,(800+ground_x,450))
    ground_x-=5
    if ground_x == -800:
        ground_x = 0

    if pygame.sprite.spritecollide(bird, pipe_group, False):
        gameOver = True 
    
   

    pygame.display.update()