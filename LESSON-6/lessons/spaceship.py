import pygame

class Spaceship:
    WIDTH = 55
    HEIGHT = 40
    VELOCITY = 5

    def __init__(self, x, y, image_path, angle):
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
        image = pygame.image.load(image_path)
        self.image = pygame.transform.rotate(
            pygame.transform.scale(image, (self.WIDTH, self.HEIGHT)),
            angle
        )
        self.health = 10

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, keys, controls, max_width, max_height, border_x=None):
        if keys[controls['left']] and self.rect.x - self.VELOCITY > 0:
            self.rect.x -= self.VELOCITY
        if keys[controls['right']] and self.rect.x + self.rect.width + self.VELOCITY < max_width:
            if border_x is None or self.rect.x + self.rect.width + self.VELOCITY < border_x:
                self.rect.x += self.VELOCITY
        if keys[controls['up']] and self.rect.y - self.VELOCITY > 0:
            self.rect.y -= self.VELOCITY
        if keys[controls['down']] and self.rect.y + self.rect.height + self.VELOCITY < max_height:
            self.rect.y += self.VELOCITY
