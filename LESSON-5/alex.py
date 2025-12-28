import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
clock=pygame.time.Clock()

bg=pygame.image.load("Lesson-5/background.png")
rocket=pygame.image.load("Lesson-5\character.png")

rocket_y=300
rocket_x=300
moves={"up":False, "right": False, "left":False}

running=True
while running:
    screen.blit(bg, (0,0))
    screen.blit(rocket, (rocket_x,rocket_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break

        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moves["up"]=True
            if event.key == pygame.K_RIGHT:
                moves["right"]=True
            if event.key == pygame.K_LEFT:
                moves["left"]=True

        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_UP:
                moves["up"]=False
            if event.key == pygame.K_RIGHT:
                moves["right"]=False
            if event.key == pygame.K_LEFT:
                moves["left"]=False

    if moves["up"]: rocket_y -=4
    if moves["left"]: rocket_x -=4
    if moves["right"]: rocket_x +=4
    rocket_y+=2



    clock.tick(60)
    pygame.display.update()

    
# git init
# git add .
# git commit -m "message"
# git push

