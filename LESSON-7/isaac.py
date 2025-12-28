import random
import pygame
pygame.init()
pygame.font.init()

screen= pygame.display.set_mode((500,500))
font = pygame.font.SysFont("Arial", 30)

class Gamecard:
    def __init__(self, url, name, pos):
        self.image= pygame.image.load(url)
        self.pos = pos
        self.text = font.render(name, 1 , "Purple")

    def draw(self):
        screen.blit(self.image, self.pos)
    
    def draw_text(self):
        screen.blit(self.text, (self.pos[0]+200, self.pos[1]+25))


running = True 

candy_crush = Gamecard("LESSON-7/candycrush.jpg", "Candy Crush", (100,50))
subwaysurfer = Gamecard("LESSON-7/subwaysurfer.png", "subwaysurfer", (100,150))
Ludo = Gamecard("LESSON-7/ludo.png", "Ludo", (100,250))
Temple_Run = Gamecard("LESSON-7/templerun.png", "Temple Run", (100,350))

games = [candy_crush, subwaysurfer, Ludo, Temple_Run]

games2 = games[:]
random.shuffle(games2)

start = []
end = []


while running:
    screen.fill("pink")
    y = 75
    for i in range(len(games)):
        games[i].draw()
        screen.blit(games2[i].text, (300, y))
        y+=100


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
            break 
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            start.append(pos)
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            end.append(pos)

    for i in range(len(end)):
        pygame.draw.circle(screen,"red", start[i],10)
        pygame.draw.circle(screen,"red", end[i],10)
        pygame.draw.line(screen, "red", start[i], end[i], 5)


    
    pygame.display.update()