import pygame
import random
import os

# =============================================================
# LESSON 2: SWAPPING AND MATCHING
# =============================================================

pygame.init()

# Window and grid settings
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 6, 6
CELL_SIZE = WIDTH // COLS
FPS = 60

# Path to candy images
CANDY_PATH = os.path.join('candy crush')

# Fallback colors (used if images are missing)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 0, 255), (0, 255, 255),
          (255, 165, 0), (128, 0, 128), (0, 128, 128),
          (255, 192, 203), (139, 69, 19), (128, 128, 0)]

# =============================================================
# IMAGE LOADER
# =============================================================
def load_candy_images():
    images = []
    for i in range(12):
        path = os.path.join(CANDY_PATH, f"{i}.png")
        if os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.smoothscale(img, (CELL_SIZE - 8, CELL_SIZE - 8))
            images.append(img)
        else:
            images.append(None)
    return images


# =============================================================
# CANDY CLASS
# =============================================================
class Candy(pygame.sprite.Sprite):
    def __init__(self, row, col, candy_type):
        super().__init__()
        self.row = row
        self.col = col
        self.type = candy_type

        img = candy_images[self.type]
        if img:
            self.image = img.copy()
        else:
            self.image = pygame.Surface((CELL_SIZE - 8, CELL_SIZE - 8), pygame.SRCALPHA)
            pygame.draw.circle(self.image, COLORS[self.type],
                               (CELL_SIZE // 2 - 4, CELL_SIZE // 2 - 4), CELL_SIZE // 3)

        self.rect = self.image.get_rect()
        self.update_position()

    def update_position(self):
        self.rect.topleft = (self.col * CELL_SIZE + 4, self.row * CELL_SIZE + 4)


# =============================================================
# BOARD CLASS (SWAP + MATCHING)
# =============================================================
class Board:
    def __init__(self):
        self.grid = [[random.randint(0, 11) for _ in range(COLS)] for _ in range(ROWS)]
        self.sprites = pygame.sprite.Group()
        self.populate_sprites()

    def populate_sprites(self):
        self.sprites.empty()
        for r in range(ROWS):
            for c in range(COLS):
                candy = Candy(r, c, self.grid[r][c])
                self.sprites.add(candy)

    def swap(self, pos1, pos2):
        """Swap two adjacent candies."""
        (r1, c1), (r2, c2) = pos1, pos2
        if abs(r1 - r2) + abs(c1 - c2) == 1:  # Adjacent only
            self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]
            self.populate_sprites()
            if not self.find_matches():
                # No match? Revert swap
                self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]
                self.populate_sprites()

    def find_matches(self):
        """Find all horizontal and vertical matches of 3+ candies."""
        matched = set()
        # Check rows
        for r in range(ROWS):
            for c in range(COLS - 2):
                if self.grid[r][c] == self.grid[r][c + 1] == self.grid[r][c + 2]:
                    matched.update({(r, c), (r, c + 1), (r, c + 2)})
        # Check columns
        for c in range(COLS):
            for r in range(ROWS - 2):
                if self.grid[r][c] == self.grid[r + 1][c] == self.grid[r + 2][c]:
                    matched.update({(r, c), (r + 1, c), (r + 2, c)})
        # Remove matches
        for r, c in matched:
            self.grid[r][c] = None
        return matched


# =============================================================
# GAME SETUP
# =============================================================
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy Crush - Lesson 2")
clock = pygame.time.Clock()

candy_images = load_candy_images()
board = Board()
selected = None
running = True

# =============================================================
# GAME LOOP
# =============================================================
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col, row = x // CELL_SIZE, y // CELL_SIZE
            if selected:
                board.swap(selected, (row, col))
                selected = None
            else:
                selected = (row, col)

    # Draw
    screen.fill((30, 30, 30))
    board.sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
