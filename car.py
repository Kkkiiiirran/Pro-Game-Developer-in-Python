import pygame
import sys
import random

# ---------- INITIAL SETUP ----------
pygame.init()

WIDTH, HEIGHT = 400, 600
LANES = [WIDTH // 4, WIDTH // 2, 3 * WIDTH // 4]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game (OOP)")

clock = pygame.time.Clock()

# ---------- LOAD IMAGES ----------
road_img = pygame.image.load("road.png")
player_img = pygame.image.load("car.png")
enemy_img = pygame.image.load("redcar.png")

road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
player_img = pygame.transform.scale(player_img, (100, 100))
enemy_img = pygame.transform.scale(enemy_img, (100, 100))


# ---------- ROAD CLASS ----------
class Road:
    def __init__(self):
        self.y = 0
        self.speed = 4

    def move(self):
        self.y += self.speed
        if self.y >= HEIGHT:
            self.y = 0

    def draw(self):
        screen.blit(road_img, (0, self.y))
        screen.blit(road_img, (0, self.y - HEIGHT))


# ---------- CAR BASE CLASS ----------
class Car:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

        # Smaller hitbox (important)
        self.hitbox = self.rect.inflate(-40, -40)

        self.speed = 5

    def update_hitbox(self):
        self.hitbox.center = self.rect.center

    def draw(self):
        screen.blit(self.image, self.rect)
       



# ---------- PLAYER CAR ----------
class PlayerCar(Car):
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

        self.update_hitbox()



# ---------- ENEMY CAR (INHERITANCE) ----------
class EnemyCar(Car):
    def __init__(self):
        x = random.choice(LANES)
        y = -120
        super().__init__(x, y, enemy_img)
        self.speed = random.randint(4, 7)

    def move(self):
        self.rect.y += self.speed
        self.update_hitbox()

        if self.rect.top > HEIGHT:
            self.rect.y = -120
            self.rect.centerx = random.choice(LANES)
            self.speed = random.randint(4, 7)



# ---------- OBJECTS ----------
road = Road()
player = PlayerCar(WIDTH // 2, HEIGHT - 120, player_img)
enemy = EnemyCar()

# ---------- MAIN LOOP ----------
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    road.move()
    player.move()
    enemy.move()

    # Collision
    if player.hitbox.colliderect(enemy.hitbox):

        print("Game Over!")
        running = False

    # Draw
    road.draw()
    player.draw()
    enemy.draw()
    pygame.display.update()

pygame.quit()
sys.exit()
