import random
import pygame
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((500,500))
font = pygame.font.SysFont("Arial", 30)

running = True 

game1 = pygame.image.load("LESSON-7/candycrush.jpg")
game2 = pygame.image.load("LESSON-7/ludo.png")
game3 = pygame.image.load("LESSON-7/subwaysurfer.png")
game4 = pygame.image.load("LESSON-7/templerun.png")

candy_crush = font.render("Candy Crush", 1, "purple")
Ludo = font.render("Ludo", 1, "purple")
Subway_Surfer = font.render("Subway Surfer", 1, "purple")
Temple_Run = font.render("Temple Run", 1, "purple")


games = [game1,game2,game3,game4]
games_text = [candy_crush, Ludo, Subway_Surfer, Temple_Run]
random.shuffle(games_text)


start = []
end = []
while running:
    screen.fill("pink")
    y = 50
    for game in games:
        screen.blit(game, (100,y))
        y+=100
    
    y=75
    for text in games_text:
        screen.blit(text, (300, y))
        y+=100
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
            break 
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONUP and start_pos:
            end_pos = pygame.mouse.get_pos()
            start.append(start_pos)
            end.append(end_pos)
    
    for pos in start:
        pygame.draw.circle(screen, color ="red", radius = 15, center = (pos))
    
    for pos in end:
        pygame.draw.circle(screen, color ="red", radius = 15, center = (pos))

    for i in range(len(start)):
        pygame.draw.line(screen, color="red", start_pos=start[i], end_pos=end[i])



    pygame.display.update()