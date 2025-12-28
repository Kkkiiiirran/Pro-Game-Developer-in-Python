import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800,600))
comic_sans = pygame.font.SysFont("Comic sans", 20)

class Spaceship:
    def __init__(self, imageurl, angle, pos, color):
        self.image  = pygame.image.load(imageurl)
        self.image  = pygame.transform.scale(self.image,(75,75))
        self.image  = pygame.transform.rotate(self.image,angle)
        self.rect   = self.image.get_rect(center = pos)
        self.bullets = []
        self.move= {"up":False, "down":False}
        self.color = color
        self.health = 10
        self.health_text = comic_sans.render(f"Health: {self.health}", 1, self.color)
    
    def fire(self, direction, enemyship):
        for bullet in self.bullets:
            bullet.rect.x+=direction

            bullet.draw()
            if bullet.rect.colliderect(enemyship.rect):
                self.bullets.remove(bullet)
                enemyship.health-=1
                enemyship.health_text = comic_sans.render(f"Health: {enemyship.health}", 1, enemyship.color)




    def movement(self):
        keys = pygame.key.get_pressed()
        if self.color == "red":
            if keys[pygame.K_w]:
                self.rect.y-=2
            if keys[pygame.K_s]:
                self.rect.y+=2

        else:
            if keys[pygame.K_UP]:
                self.rect.y-=2
            if keys[pygame.K_DOWN]:
                self.rect.y+=2



class Bullet:
    def __init__(self, pos, color):
        self.rect = pygame.Rect(pos, (10,10))
        self.color = color
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
   


bg = pygame.image.load('LESSON-6\Assets\space.png')
bg = pygame.transform.scale(bg,(800,600))

red_ship= Spaceship('LESSON-6\Assets\spaceship_red.png', +90, (100,300), "red")
yellow_ship= Spaceship('LESSON-6\Assets\spaceship_yellow.png', -90,(700,300), "yellow")

gameover_text = comic_sans.render("GAMEOVER", 1, "WHITE")


running = True
gameover = False
while running:

    screen.blit(bg, (0,0))
    if red_ship.health <=0 or yellow_ship.health<=0:
        gameover= True

    if gameover:
        screen.blit(gameover_text, (400,300))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False   
                break
        
        pygame.display.update() 
        continue
    
    screen.blit(red_ship.image,red_ship.rect.topleft)
    screen.blit(yellow_ship.image,yellow_ship.rect.topleft)
    screen.blit(red_ship.health_text, (50,20))
    screen.blit(yellow_ship.health_text, (650,20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                red_bullet = Bullet(red_ship.rect.center, "red")
                red_ship.bullets.append(red_bullet)
            
            if event.key == pygame.K_l:
                yellow_bullet = Bullet(yellow_ship.rect.center, "yellow")
                yellow_ship.bullets.append(yellow_bullet)
    
    red_ship.movement()
    yellow_ship.movement()
    
    red_ship.fire(+2, yellow_ship)
    yellow_ship.fire(-2, red_ship)

    pygame.display.update()                                                                                                                                          
                                                                           