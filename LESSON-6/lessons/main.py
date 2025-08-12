import pygame
from spaceship import Spaceship
from bullets import BulletManager
from setup import GameSetup

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

def main():
    game = GameSetup()
    bullet_mgr = BulletManager()

    yellow = Spaceship(100, 300, "LESSON-6\Assets\spaceship_yellow.png", 90)
    red = Spaceship(700, 300, "LESSON-6\Assets\spaceship_red.png", 270)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    bullet_mgr.fire(yellow, 'yellow', 'right')
                if event.key == pygame.K_RSHIFT:
                    bullet_mgr.fire(red, 'red', 'left')

            if event.type == RED_HIT:
                red.health -= 1
            if event.type == YELLOW_HIT:
                yellow.health -= 1

        winner = ""
        if red.health <= 0:
            winner = "Yellow Wins!"
        elif yellow.health <= 0:
            winner = "Red Wins!"
        if winner:
            game.draw_winner(winner)
            break

        keys = pygame.key.get_pressed()
        yellow.move(keys, {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s}, game.WIDTH, game.HEIGHT, game.border.x)
        red.move(keys, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}, game.WIDTH, game.HEIGHT)

        bullet_mgr.move_and_check(red, yellow, pygame.event.get(), RED_HIT, YELLOW_HIT, game.WIDTH)
        game.draw_window(red, yellow, bullet_mgr)

if __name__ == "__main__":
    main()
