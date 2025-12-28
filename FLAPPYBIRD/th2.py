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
            self.rect.y+=self.velocity
 


class Pipe(pygame.sprite.Sprite):
    def __init__(self,invert,y):
        super().__init__()
        self.image = pygame.image.load("FLAPPYBIRD/pipe.png")
        self.pipe = self.image
        self.rect = self.pipe.get_rect()
        self.y = y
        self.x =600
        self.invert = invert
        self.pipe_gap = 75

        if self.invert == True:
            self.rect.topleft = (self.x,self.y+self.pipe_gap)
        else:
            self.image = pygame.transform.flip(self.image, False, True)
            
            self.rect.bottomleft = (self.x,self.y-self.pipe_gap)
        
    def update(self):
        self.rect.x -= 10
        if self.rect.x<0:
            self.kill()
        
        
        #self.rect.topleft = (self.x,random.randint(0,450))

    
bird = Bird(300,300)
pipe_group = pygame.sprite.Group()

prev_time = pygame.time.get_ticks()
# pipe = Pipe(True)
# pipe2 = Pipe(False)
# pipe_group.add(pipe)
# pipe_group.add(pipe2)


ground_x = 0
while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    
    screen.blit(bird.image,(bird.rect))
    
    ground_x-=5
    if ground_x == -800:
        ground_x = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    curr_time = pygame.time.get_ticks()
    if curr_time-prev_time>2000:
        y = random.randint(150,300)
        pipe = Pipe(True, y)
        pipe2 = Pipe(False, y)
        pipe_group.add(pipe)
        pipe_group.add(pipe2)
        prev_time = curr_time



    bird.update()
    pipe_group.update()
    pipe_group.draw(screen)
    screen.blit(ground,(ground_x,450))
    screen.blit(ground,(800+ground_x,450))

    if pygame.sprite.spritecollide(bird, pipe_group, False):
        

    pygame.display.update()