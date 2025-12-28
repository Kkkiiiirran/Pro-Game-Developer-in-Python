import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))

running = True

bg = pygame.image.load("LESSON-5/background.png")
rocket = pygame.image.load("LESSON-5/character.png")
x = 50
y = 50


def movement(keys):
    global x,y
    if keys[pygame.K_RIGHT]:
        x+=10
    elif keys[pygame.K_LEFT]:
        x-=10
    if keys[pygame.K_DOWN]:
        y+=10
    elif keys[pygame.K_UP]:
        y-=10

while running:
    clock.tick(60)
    screen.blit(bg, (0,0))
    screen.blit(rocket, (x,y))


    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type==pygame.QUIT:
            running=False
            break

    movement(keys)


    pygame.display.update()