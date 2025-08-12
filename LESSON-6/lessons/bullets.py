import pygame
class BulletManager:
    BULLET_VEL = 7
    MAX_BULLETS = 3

    def __init__(self):
        self.red_bullets = []
        self.yellow_bullets = []

    def fire(self, shooter, color, direction):
        if color == 'yellow' and len(self.yellow_bullets) < self.MAX_BULLETS:
            bullet = pygame.Rect(shooter.rect.x + shooter.rect.width, shooter.rect.y + shooter.rect.height // 2 - 2, 10, 5)
            self.yellow_bullets.append(bullet)
        elif color == 'red' and len(self.red_bullets) < self.MAX_BULLETS:
            bullet = pygame.Rect(shooter.rect.x, shooter.rect.y + shooter.rect.height // 2 - 2, 10, 5)
            self.red_bullets.append(bullet)

    def move_and_check(self, red_ship, yellow_ship, events, RED_HIT, YELLOW_HIT, width):
        for bullet in self.yellow_bullets[:]:
            bullet.x += self.BULLET_VEL
            if red_ship.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                self.yellow_bullets.remove(bullet)
            elif bullet.x > width:
                self.yellow_bullets.remove(bullet)

        for bullet in self.red_bullets[:]:
            bullet.x -= self.BULLET_VEL
            if yellow_ship.rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                self.red_bullets.remove(bullet)
            elif bullet.x < 0:
                self.red_bullets.remove(bullet)

    def draw(self, win):
        for b in self.red_bullets:
            pygame.draw.rect(win, (255, 0, 0), b)
        for b in self.yellow_bullets:
            pygame.draw.rect(win, (255, 255, 0), b)
