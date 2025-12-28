import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600,600))
running = True

bg = pygame.image.load("LESSON-5/background.png")
rocket = pygame.image.load("LESSON-5/character.png")

y = 250
x = 250


moves = {"up": False, "right": False, "left":False, "a":False}
while running:
    clock.tick(60)
    screen.blit(bg, (0,0))
    screen.blit(rocket, (x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moves["up"] = True
            if event.key == pygame.K_LEFT:
                moves["left"] = True
            if event.key == pygame.K_RIGHT:
                moves["right"] = True
            
            if event.key == pygame.K_a:
                moves['a'] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moves["up"] = False
            if event.key == pygame.K_LEFT:
                moves["left"] = False
    
            if event.key == pygame.K_RIGHT:
                moves["right"] = False
            if event.key == pygame.K_a:
                moves['a'] = False

    if moves["up"]: y-=4
    if moves["left"]:x-=4
    if moves["right"]:x+=4
    if moves["a"]: y-=25

    y+=2
    pygame.display.update()

    