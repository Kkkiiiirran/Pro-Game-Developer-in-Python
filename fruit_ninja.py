import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# ---------- SCREEN SETUP ----------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Fruit Ninja (OOP)")
clock = pygame.time.Clock()

# ---------- LOAD IMAGES ----------
apple_img = pygame.transform.scale(pygame.image.load("apple.png"), (60, 60))
orange_img = pygame.transform.scale(pygame.image.load("orange.png"), (60, 60))
bomb_img = pygame.transform.scale(pygame.image.load("bomb.png"), (60, 60))
bg = pygame.image.load("board.png")

# ---------- LOAD SOUNDS ----------
slice_sound = pygame.mixer.Sound("blade.mp3")
bomb_sound = pygame.mixer.Sound("bomb.mp3")

slice_sound.set_volume(0.6)
bomb_sound.set_volume(0.8)

pygame.mixer.music.load("bgmusic.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

# ---------- FONT ----------
score_font = pygame.font.SysFont(None, 36)
game_over_font = pygame.font.SysFont(None, 64)

# ---------- FRUIT CLASS ----------
class Fruit:
    def __init__(self, image):
        self.image = image
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT + 50
        self.speed = random.randint(2, 4)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        self.y -= self.speed
        self.rect.center = (self.x, self.y)

    def draw(self):
        screen.blit(self.image, self.rect)

    def is_sliced(self, pos):
        return self.rect.collidepoint(pos)


# ---------- BOMB CLASS ----------
class Bomb(Fruit):
    def __init__(self):
        super().__init__(bomb_img)


# ---------- SLICE EFFECT ----------
class SliceEffect:
    def __init__(self, pos):
        self.x, self.y = pos
        self.life = 8

    def update(self):
        self.life -= 1

    def draw(self):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (self.x - 30, self.y + 30),
            (self.x + 30, self.y - 30),
            4
        )

    def is_dead(self):
        return self.life <= 0


# ---------- GAME DATA ----------
objects = []
slice_effects = []
score = 0
running = True
game_over = False

# ---------- MAIN LOOP ----------
while running:
    clock.tick(60)
    screen.blit(bg, (0, 0))

    # ---- EVENTS ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            slice_effects.append(SliceEffect(mouse_pos))

            for obj in objects[:]:
                if obj.is_sliced(mouse_pos):
                    if isinstance(obj, Bomb):
                        bomb_sound.play()
                        game_over = True
                    else:
                        slice_sound.play()
                        score += 1          # ⭐ SCORE INCREASE
                        objects.remove(obj)

    # ---- SPAWN OBJECTS ----
    if not game_over and random.randint(1, 40) == 1:
        if random.randint(1, 5) == 1:
            objects.append(Bomb())
        else:
            objects.append(Fruit(random.choice([apple_img, orange_img])))

    # ---- UPDATE OBJECTS ----
    if not game_over:
        for obj in objects[:]:
            obj.move()
            if obj.y < -50:
                objects.remove(obj)

    for effect in slice_effects[:]:
        effect.update()
        if effect.is_dead():
            slice_effects.remove(effect)

    # ---- DRAW OBJECTS ----
    for obj in objects:
        obj.draw()

    for effect in slice_effects:
        effect.draw()

    # ---- DRAW SCORE ----
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    # ---- GAME OVER TEXT ----
    if game_over:
        text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2))

    pygame.display.update()

pygame.quit()
sys.exit()
