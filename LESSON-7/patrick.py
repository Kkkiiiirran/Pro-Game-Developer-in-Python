import pygame
pygame.init()
screen= pygame.display.set_mode((500,500))

running = True 

while running:
    screen.fill("pink")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
            break 

        if event.type== pygame.MOUSEBUTTONDOWN:
            print("helloo")
            start_pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()
            print("bye")

            pygame.draw.line(screen, "red", start_pos, end_pos,5)
            pygame.display.update()
  
    pygame.display.update()