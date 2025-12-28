import pygame
import time
class Spaceship():
    def __init__(self, image_url, angle, x, y):
        self.image = pygame.image.load(image_url)
        self.image = pygame.transform.scale(self.image, (70,70))
        self.image = pygame.transform.rotate(self.image, angle)
        self.x = x
        self.y = y



red_ship = Spaceship("LESSON-6/Assets/spaceship_red.png", 90, 100, 250)
yellow_ship = Spaceship("LESSON-6/Assets/spaceship_yellow.png", -90, 500, 250)


pygame.init()

screen = pygame.display.set_mode((700,500))


bg = pygame.image.load("LESSON-6/Assets/space.png")
bg = pygame.transform.scale(bg, (700,500))


KEYS = {"up": False, "down": False}

running = True

while running:
    screen.blit(bg, (0,0))
    screen.blit(red_ship.image, (red_ship.x, red_ship.y))
    screen.blit(yellow_ship.image, (yellow_ship.x, yellow_ship.y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                KEYS["up"] = True
            
            
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                KEYS["up"] = False
    
    if KEYS["up"]:
        red_ship.y-=4

    if KEYS["down"]:
        red_ship.y+=4




    time.sleep(0.05)
    pygame.display.update()




# screen
# fill
# images
# characters
# keyboard
# mouse clicks
# transform









