import pygame
pygame.init()
screen=pygame.display.set_mode((1000, 1200))
bg=screen.fill("black")
center_x=screen.get_width() //2

class Spaceship:
    def __init__(self, player):
        self.player=player
        self.speed_x=2
        self.speed_y=2
        self.bullets = []
        
        if self.player==1:
            self.y, self.x=600,100
            self.image=pygame.image.load("LESSON-6/spaceship1.png")
           
        elif self.player==2:
            self.y, self.x=600,600
            self.image=pygame.image.load("LESSON-6/spaceship2.png")

        self.rect = self.image.get_rect(center = ( self.y, self.x))

    def fire(self):
        for bullet in self.bullets:
            bullet.rect.x-=4
            bullet.draw()

    def draw(self):
      
        
        screen.blit(self.image, (self.rect.topleft))
        pygame.draw.line(screen,(255,255,255) ,(center_x, 0), (center_x, 1200), 5)

    def movements(self):
        keys=pygame.key.get_pressed()
        if self.player==1:
            
            if keys[pygame.K_a]: self.rect.x -=self.speed_x

            if keys[pygame.K_w]: self.rect.y -=self.speed_y
            if keys[pygame.K_s]: self.rect.y +=self.speed_y


            if keys[pygame.K_d]:
                if self.rect.x<=1000: 
                    self.rect.x +=self.speed_x
        if self.player==2:
            # if self.x>=1000:
            if keys[pygame.K_LEFT]: self.rect.x -=self.speed_x
            if keys[pygame.K_UP]: self.rect.y -=self.speed_y
            if keys[pygame.K_DOWN]: self.rect.y +=self.speed_y
            if keys[pygame.K_RIGHT]: self.rect.x +=self.speed_x


class Bullet:
    def __init__(self, pos,color):
        self.pos = pos
        self.color = color
        self.rect = pygame.Rect(pos, (20,10))
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        



p1=Spaceship(1)
p2=Spaceship(2)
running=True
while running:
    screen.fill("black")
    p1.draw()
    p2.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
    
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
                running=False
                break
        
            if event.key == pygame.K_e:
                player1_bullet = Bullet(p1.rect.center, "yellow")

            if event.key == pygame.K_l:
                player2_bullet = Bullet(p2.rect.center, "pink")
                p2.bullets.append(player2_bullet)

            
    p1.movements()
    p2.movements()
    p2.fire()

    pygame.display.update()