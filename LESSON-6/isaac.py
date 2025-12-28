import pygame
class Spaceship:
    
    def __init__(self,image,angle,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(60,60))
        self.image = pygame.transform.rotate(self.image,angle)
        self.move = {"up":False,"down":False}
        self.bullets = []
        self.rect = self.image.get_rect(center = (self.x,self.y))
        self.health = 10
        self.health_text = health_font.render(f"Health: {self.health}", 1, "white")
    
    def detect_colision(self,enemyship):
        for bullet in self.bullets:
            if bullet.rect.colliderect(enemyship.rect):
                self.bullets.remove(bullet)
                enemyship.health-=1
                enemyship.health_text = health_font.render(f"Health: {enemyship.health}", 1, "white")
                if enemyship.health==0:
                    return True
                    

    
    def handle_movement(self):
        if self.move["up"]:
            self.rect.y-=4
        elif self.move["down"]:
            self.rect.y+=4

        for bullet in self.bullets:
            if bullet.rect.x<=0 or bullet.rect.x>=1000:
                self.bullets.remove(bullet)
            else:
                bullet.fire()
                bullet.draw()
            


class Bullet:
    def __init__(self,color,center):
        self.x,self.y = center
        self.color = color
        self.rect = pygame.Rect(self.x,self.y, 10,10)

    def fire(self):
        if self.color == "red":
            self.rect.x+=5
        else:
            self.rect.x-=5

    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)



pygame.init()
pygame.font.init()

health_font = pygame.font.SysFont("Times Now Roman", 30)

screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

bg = pygame.image.load("LESSON-6\Assets\space.png")
bg = pygame.transform.scale(bg,(1000,600))
red_spaceship = Spaceship("LESSON-6\Assets\spaceship_red.png",(90),100,100)
yellow_spaceship = Spaceship("LESSON-6\Assets\spaceship_yellow.png",(-90),800,100)

gameover_text = health_font.render("GAMEOVER", 1, "white")
running = True
move = {"up": False, "down": False}

# ex = render(red_spaceship.health, 0, "red", background=None)
gameover = False
while running:
    clock.tick(60)
    screen.blit(bg,(0,0))
  
    if gameover:
        screen.blit(gameover_text, (500,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running=False 
                break
    else:
        screen.blit(red_spaceship.image,(red_spaceship.rect.topleft))
        screen.blit(yellow_spaceship.image,(yellow_spaceship.rect.topleft))
        screen.blit(red_spaceship.health_text, (30,30))
        screen.blit(yellow_spaceship.health_text, (840,30))
        pygame.draw.line(screen,"white", (500,0), (500,600), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    red_spaceship.move["up"] = True
                if event.key == pygame.K_s:
                    red_spaceship.move["down"] = True

                if event.key == pygame.K_a:
                    red_spaceship_bullet = Bullet("red",red_spaceship.rect.center)
                    red_spaceship.bullets.append(red_spaceship_bullet)

                if event.key == pygame.K_l:
                    yellow_spaceship_bullet = Bullet("yellow",yellow_spaceship.rect.center)
                    yellow_spaceship.bullets.append(yellow_spaceship_bullet)
                

                if event.key == pygame.K_UP:
                    yellow_spaceship.move["up"] = True
                if event.key == pygame.K_DOWN:
                    yellow_spaceship.move["down"] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    red_spaceship.move["up"] = False
                if event.key == pygame.K_UP:
                    yellow_spaceship.move["up"] = False

                if event.key == pygame.K_s:
                    red_spaceship.move["down"] = False

                if event.key == pygame.K_DOWN:
                    yellow_spaceship.move["down"] = False


        red_spaceship.handle_movement()
        yellow_spaceship.handle_movement()
        if red_spaceship.detect_colision(yellow_spaceship):
            gameover = True
        if yellow_spaceship.detect_colision(red_spaceship):
            gameover=True
    pygame.display.update()