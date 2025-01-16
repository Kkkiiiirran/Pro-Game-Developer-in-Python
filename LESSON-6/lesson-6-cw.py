import pygame
import os

class Game:
    WIDTH, HEIGHT = 900, 500
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    FPS = 60
    VEL = 5
    BULLET_VEL = 7
    MAX_BULLETS = 3
    SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

    YELLOW_HIT = pygame.USEREVENT + 1
    RED_HIT = pygame.USEREVENT + 2

    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("First Game!")

        self.health_font = pygame.font.SysFont('comicsans', 40)
        self.winner_font = pygame.font.SysFont('comicsans', 100)

        self.border = pygame.Rect(self.WIDTH // 2 - 5, 0, 10, self.HEIGHT)

        self.yellow_spaceship = self.load_spaceship(
            os.path.join('LESSON-6\Assets', 'spaceship_yellow.png'), 90
        )
        self.red_spaceship = self.load_spaceship(
            os.path.join('LESSON-6\Assets', 'spaceship_red.png'), 270
        )
        self.space_bg = pygame.transform.scale(
            pygame.image.load(os.path.join('LESSON-6\Assets', 'space.png')),
            (self.WIDTH, self.HEIGHT),
        )

    def load_spaceship(self, path, angle):
        image = pygame.image.load(path)
        return pygame.transform.rotate(
            pygame.transform.scale(image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)),
            angle,
        )

    def draw_window(self, red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
        self.win.blit(self.space_bg, (0, 0))
        pygame.draw.rect(self.win, self.BLACK, self.border)

        red_health_text = self.health_font.render(f"Health: {red_health}", 1, self.WHITE)
        yellow_health_text = self.health_font.render(f"Health: {yellow_health}", 1, self.WHITE)
        self.win.blit(red_health_text, (self.WIDTH - red_health_text.get_width() - 10, 10))
        self.win.blit(yellow_health_text, (10, 10))

        self.win.blit(self.yellow_spaceship, (yellow.x, yellow.y))
        self.win.blit(self.red_spaceship, (red.x, red.y))

        for bullet in red_bullets:
            pygame.draw.rect(self.win, self.RED, bullet)
        for bullet in yellow_bullets:
            pygame.draw.rect(self.win, self.YELLOW, bullet)

        pygame.display.update()

    def handle_movement(self, keys_pressed, obj, controls):
        if keys_pressed[controls['left']] and obj.x - self.VEL > 0:
            obj.x -= self.VEL
        if keys_pressed[controls['right']] and obj.x + self.VEL + obj.width < self.WIDTH:
            obj.x += self.VEL
        if keys_pressed[controls['up']] and obj.y - self.VEL > 0:
            obj.y -= self.VEL
        if keys_pressed[controls['down']] and obj.y + self.VEL + obj.height < self.HEIGHT:
            obj.y += self.VEL

    def handle_bullets(self, yellow_bullets, red_bullets, yellow, red):
        for bullet in yellow_bullets:
            bullet.x += self.BULLET_VEL
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.RED_HIT))
                yellow_bullets.remove(bullet)
            elif bullet.x > self.WIDTH:
                yellow_bullets.remove(bullet)

        for bullet in red_bullets:
            bullet.x -= self.BULLET_VEL
            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.YELLOW_HIT))
                red_bullets.remove(bullet)
            elif bullet.x < 0:
                red_bullets.remove(bullet)

    def draw_winner(self, text):
        draw_text = self.winner_font.render(text, 1, self.WHITE)
        self.win.blit(draw_text, (self.WIDTH / 2 - draw_text.get_width() / 2, self.HEIGHT / 2 - draw_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(5000)

    def main(self):
        red = pygame.Rect(700, 300, self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)
        yellow = pygame.Rect(100, 300, self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)

        red_bullets = []
        yellow_bullets = []

        red_health = 10
        yellow_health = 10

        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT and len(yellow_bullets) < self.MAX_BULLETS:
                        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                        yellow_bullets.append(bullet)
                    if event.key == pygame.K_RSHIFT and len(red_bullets) < self.MAX_BULLETS:
                        bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                        red_bullets.append(bullet)

                if event.type == self.RED_HIT:
                    red_health -= 1

                if event.type == self.YELLOW_HIT:
                    yellow_health -= 1

            winner_text = ""
            if red_health <= 0:
                winner_text = "Yellow Wins!"
            if yellow_health <= 0:
                winner_text = "Red Wins!"

            if winner_text:
                self.draw_winner(winner_text)
                break

            keys_pressed = pygame.key.get_pressed()
            self.handle_movement(keys_pressed, yellow, {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s})
            self.handle_movement(keys_pressed, red, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN})

            self.handle_bullets(yellow_bullets, red_bullets, yellow, red)

            self.draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

        self.main()

if __name__ == "__main__":
    Game().main()