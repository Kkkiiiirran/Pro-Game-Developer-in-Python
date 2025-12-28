import pygame
pygame.init()
pygame.font.init()

screen=pygame.display.set_mode((2000, 1200))
bg=screen.fill("black")
center_x=screen.get_width() //2

comic_sans = pygame.font.SysFont("Comic Sans", 40)



class Spaceship:
    def __init__(self, player):
        self.player=player
        self.speed_x=2
        self.speed_y=2

        if self.player==1:
            self.y, self.x=600,100
            self.image=pygame.image.load("LESSON-6\Assets\spaceship_red.png")
          
        elif self.player==2:
            self.y, self.x=600,1900
            self.image=pygame.image.load("LESSON-6\Assets\spaceship_yellow.png")
        
        
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.bullets = []

        

    def draw(self):
        screen.blit(self.image, (self.rect.topleft))
        pygame.draw.line(screen,(255,255,255) ,(center_x, 0), (center_x, 1200), 5)

    def fire(self):
        for bullet in self.bullets:
            if self.player==1:
                bullet.rect.x+=3
            else:
                bullet.rect.x-=3
            bullet.draw()

  
        
    def movements(self):
        keys=pygame.key.get_pressed()
        if self.player==1:
            if self.rect.x<=850:
                if keys[pygame.K_d]: self.rect.x +=self.speed_x
            if keys[pygame.K_w]: self.rect.y -=self.speed_y
            if keys[pygame.K_s]: self.rect.y +=self.speed_y
            if keys[pygame.K_a]: self.rect.x -=self.speed_x
        if self.player==2:
            if self.rect.x>=1000:
                if keys[pygame.K_LEFT]: self.rect.x -=self.speed_x
            if keys[pygame.K_UP]: self.rect.y -=self.speed_y
            if keys[pygame.K_DOWN]: self.rect.y +=self.speed_y
            if keys[pygame.K_RIGHT]: self.rect.x +=self.speed_x

class Bullet:
    def __init__(self, colour, position):
        self.colour=colour
        self.rect=pygame.Rect((position), (15,10))
  

    def draw(self):
        pygame.draw.rect(screen, self.colour, self.rect)

    
        
p1=Spaceship(1)
p2=Spaceship(2)
running=True

sample_text = comic_sans.render("hello", 1, "red")



while running:
    screen.fill("black")
    p1.draw()
    p2.draw()
    screen.blit(sample_text, (400,400))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
                break
            if event.key == pygame.K_e:
                red_b = Bullet("red",  p1.rect.center)
                p1.bullets.append(red_b)
                
            if event.key == pygame.K_l:
                yellow_b = Bullet("yellow",  p2.rect.center)
                p2.bullets.append(yellow_b)

    p1.movements()
    p2.movements()
    p1.fire()
    p2.fire()
   
    pygame.display.update()