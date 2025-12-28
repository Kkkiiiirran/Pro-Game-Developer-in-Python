import random
import pygame

class Recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("LESSON-10/item1.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()



pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))

background = pygame.image.load("LESSON-10/bground.png")
# background = pygame.image.load(img)
bg = pygame.transform.scale(background, (500,500))


all_sprites = pygame.sprite.Group()
recycle_group = pygame.sprite.Group()


for i in range(10):
    obj = Recyclable()
    obj.rect.x = random.randint(50,450)
    obj.rect.y = random.randint(50,450)
    recycle_group.add(obj)






playing = True
while playing:
    clock.tick(30)
    screen.blit(bg,(0,0))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            playing=False
    
    recycle_group.draw(screen)

    pygame.display.update()

