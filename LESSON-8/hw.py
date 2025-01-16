import pygame
import random
import sys

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)

block_size = 20


clock = pygame.time.Clock()

class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((block_size, block_size))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((block_size, block_size))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            random.randint(0, (screen_width - block_size) // block_size) * block_size,
            random.randint(0, (screen_height - block_size) // block_size) * block_size,
        )

def snake_game():

    snake = [SnakeSegment(100, 100)]
    snake_group = pygame.sprite.Group(snake)
    direction = (block_size, 0)  # Start moving right

  
    food = Food()
    food_group = pygame.sprite.GroupSingle(food)


    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, block_size):
            direction = (0, -block_size)
        if keys[pygame.K_DOWN] and direction != (0, -block_size):
            direction = (0, block_size)
        if keys[pygame.K_LEFT] and direction != (block_size, 0):
            direction = (-block_size, 0)
        if keys[pygame.K_RIGHT] and direction != (-block_size, 0):
            direction = (block_size, 0)

       
        head_x, head_y = snake[0].rect.topleft
        new_head = SnakeSegment(head_x + direction[0], head_y + direction[1])
        snake.insert(0, new_head)
        snake_group.add(new_head)

        if pygame.sprite.spritecollideany(new_head, food_group):
            score += 1
            food_group.empty()
            food = Food()
            food_group.add(food)
        else:
            tail = snake.pop()
            snake_group.remove(tail)

      
        if (
            new_head.rect.left < 0
            or new_head.rect.right > screen_width
            or new_head.rect.top < 0
            or new_head.rect.bottom > screen_height
        ):
            running = False
        for segment in snake[1:]:
            if new_head.rect.colliderect(segment.rect):
                running = False

        screen.fill(BLACK)
        snake_group.draw(screen)
        food_group.draw(screen)

     
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)  

    # Game over screen
    game_over_text = font.render("Game Over! Press any key to exit.", True, WHITE)
    screen.blit(game_over_text, (screen_width // 2 - 200, screen_height // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  
    pygame.quit()
    sys.exit()

snake_game()
