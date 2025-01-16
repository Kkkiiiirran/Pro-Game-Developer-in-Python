import pygame

pygame.init()
pygame.display.set_caption('Rocket in Space')

WIDTH=700
HEIGHT=500
screen = pygame.display.set_mode([WIDTH,HEIGHT])

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("LESSON-8/character.png")
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()
    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

sprites = pygame.sprite.Group()

def startgame():
    player = Player()
    sprites.add(player)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                exit(0)
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(pygame.image.load("LESSON-8/background.png"),(0,0))
        
        sprites.draw(screen)
    
        pygame.display.update()


startgame()


          