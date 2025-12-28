import pygame
import time
pygame.init()
# clock = pygame.time.Clock()
screen = pygame.display.set_mode([500,500])
#move = 0
class Paddle:

    def __init__(self,x,y,width,height,move,movey):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = move
        self.movey =movey
        self.lives = 3
    def create_rect(self):
        rect = pygame.Rect((self.x,self.y),(self.width,self.height))
        return rect
    def draw(self):
        rect = self.create_rect()
        pygame.draw.rect(screen,(255,125,125),rect)
    def change_move(self,change,changey):
        self.move=change
        self.movey = changey
    def movement(self):
        self.x += self.move
        self.y+=self.movey
    def invisa_rect(self,a):
        invisa_rect = pygame.Rect((self.x+a,self.y+a),(self.width+20,self.height+20))
       
        return invisa_rect
    def change_lives(self):
        # if self.lives>=0:
        self.lives-=1
    
    

class Ball:
    def __init__(self,radius,x,y):
        self.radius = radius
        self.x = x
        self.y = y
        self.change_x = -5
        self.change_y = -5
    def draw(self):
        pygame.draw.circle(screen,center=(self.x,self.y),radius = self.radius,color = (125,125,255))
    def collide(self,paddle):
        rect = pygame.Rect(self.x-self.radius,self.y-self.radius,self.radius*2,self.radius*2)
        if paddle.colliderect(rect):
            self.change_y*=-1
            # self.change_x*=mx
    def move(self):
        self.x+=self.change_x
        self.y += self.change_y
        if self.x >= 500 or self.x <=0:
            self.change_x*=-1
        if self.y<=0:
            self.change_y*=-1
        if self.y>=500:
            return True
        
        
        
        

r = Paddle(250,450,100,30,0,0)

c = Ball(10,20,20)
while True:
    # clock.tick(60) 
    #pygame.draw.rect(screen,(255,125,125),rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                r.change_move(-5,0)
            if event.key == pygame.K_RIGHT:
                r.change_move(5,0)
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                r.change_move(0,0)
            if event.key == pygame.K_RIGHT:
                r.change_move(0,0)
        
        
    screen.fill((0,0,0))
    r.draw()
    #r2.draw()
    if c.move():
        if r.lives!= 0:
            r.change_lives()
            print(r.lives)
            c.x = 20
            c.y = 20
        if r.lives == 0:
            screen.fill((0,0,0))

    c.collide(r.create_rect())
   
    c.draw()
    r.movement()

    time.sleep(0.05)

    pygame.display.update()