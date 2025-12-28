import pygame 
import random
class Recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("LESSON-10/item1.png")
        self.image = pygame.transform.scale(self.image, (50,70))
        self.rect =self.image.get_rect(center = (random.randint(50,450),random.randint(50,450)))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("LESSON-10/bin.png")
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect =self.image.get_rect(center = (0,0))



pygame.init()

screen = pygame.display.set_mode((500,500))

running = True 

bg = pygame.image.load("LESSON-10/background.png")





recyclable_group = pygame.sprite.Group()

for i in range(10):
    obj = Recyclable()
    recyclable_group.add(obj)


bin = Bin()



while running:
    screen.blit(bg, (0,0))
    screen.blit(bin.image, bin.rect.center)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False 
            break 
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        bin.rect.x-=2
    if keys[pygame.K_RIGHT]:
        bin.rect.x+=2
    if keys[pygame.K_UP]:
        bin.rect.y-=2
    if keys[pygame.K_DOWN]:
        bin.rect.y+=2



    
    
    pygame.sprite.spritecollide(bin, recyclable_group, 1)
    

    recyclable_group.draw(screen)
    
    pygame.display.update()

