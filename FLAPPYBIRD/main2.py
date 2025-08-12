import pygame,random

pygame.init()

WIDTH=800
HEIGHT=900
screen=pygame.display.set_mode((WIDTH,HEIGHT))
fps = 60


pipegap=150
pipe_frequency=1500#ms


last_pipe=pygame.time.get_tics()-pipe_frequency


pass_pipe=False
fly=False
GAME_OVER=False
pygame.display.set_caption("drib yppalf")
scroll_ground=0
scroll_speed=4
#load images
bg=pygame.image.load("flappybord-assets-main/bg.png")
ground=pygame.image.load("flappybord-assets-main/ground.png")


class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        
        for i in range(3):
            img=pygame.image.load(f"flappybord-assets-main/bird"+str(i+1)+".png")
            #img=pygame.image.load(f"flappybord-assets-main/bird{i+1}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.velocity=0

    def update(self):
        if fly:
            self.velocity+=0.5
            if self.velocity>8:
                self.velocity=8
            if self.rect.bottom<700:
                self.rect.y+=self.velocity
        
        if not GAME_OVER:
            if pygame.mouse.get_pressed()[0]==1:
                self.velocity=-10
        
            flap_cooldown=5
            self.counter+=1
            if self.counter>flap_cooldown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
            self.image=self.images[self.index]
            self.image=pygame.transform.rotate(self.image,self.velocity*-2)
        else:
            self.image=pygame.transform.rotate(self.image,90)
            
class Pipe(pygame.sprite.Sprite):
    def __init__ (self,x,y,pos):
        pygame.sprite.Sprite.__init__(self) #super
        self.image=pygame.image.load("flappybord-assets-main/pipe.png")
        self.rect=self.image.get_rect()
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)#false horizantil True vertical
            self.rect.bottomleft=[x,y-int(pipegap/2)]
        if pos==-1:
            self.rect.topleft=[x,y-int(pipegap/2)]
    def update(self):
        self.rect.x-=scroll_speed
        if self.rect.right<0:
            self.kill()


bird_group=pygame.sprite.Group()
pipe_group=pygame.sprite.Group()
drib=Bird(100,HEIGHT/2)
bird_group.add(drib)

run=True
while run:
    screen.blit(bg,(0,0))
    bird_group.draw(screen)
    pipe_group.draw(screen)
    bird_group.update()
    screen.blit(ground,(scroll_ground,HEIGHT-200))

    if drib.rect.bottom>=700:
        GAME_OVER=True
        print("hello world")
        fly=False
    if not GAME_OVER and fly:
        scroll_ground=scroll_ground-scroll_speed
        if scroll_ground<-35:
            scroll_ground=0

        time_now=pygame.time.get_tics()
        if time_now-last_pipe>pipe_frequency:
            pipe_height=random.randint(-100,100)
            b_pipe=Pipe(WIDTH,HEIGHT/2+pipe_height,-1)
            t_pipe=Pipe(WIDTH,HEIGHT/2+pipe_height,1)
            pipe_group.add(b_pipe)
            pipe_group.add(t_pipe)
            last_pipe=time_now
        pipe_group.update()


        
    
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False 
            pygame.quit()
        if e.type==pygame.MOUSEBUTTONDOWN and fly==False and GAME_OVER==False:
            fly=True
    pygame.display.update()