import pygame
import random
import os

pygame.init()

# =============================================================
# SETTINGS
# =============================================================
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 6, 6
CELL_SIZE = WIDTH // COLS
FPS = 60

CANDY_PATH = os.path.join('candy crush')

COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (255, 165, 0), (128, 0, 128), (0, 128, 128),
    (255, 192, 203), (139, 69, 19), (128, 128, 0)
]

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
        self.image = self.make_image()
        self.rect = self.image.get_rect()
        self.update_position()

    def make_image(self):
        img = candy_images[self.type]
        if img:
            return img.copy()
        surf = pygame.Surface((CELL_SIZE - 8, CELL_SIZE - 8), pygame.SRCALPHA)
        pygame.draw.circle(surf, COLORS[self.type],
                           (CELL_SIZE // 2 - 4, CELL_SIZE // 2 - 4), CELL_SIZE // 3)
        return surf

    def update_position(self):
        self.rect.topleft = (self.col * CELL_SIZE + 4, self.row * CELL_SIZE + 4)


# =============================================================
# BOARD CLASS
# =============================================================
class Board:
    def __init__(self):
        # Initialize grid values
        self.grid = [[random.randint(0, 11) for _ in range(COLS)] for _ in range(ROWS)]
        # Create persistent candy sprites
        self.sprites = pygame.sprite.Group()
        self.candies = [[Candy(r, c, self.grid[r][c]) for c in range(COLS)] for r in range(ROWS)]
        for row in self.candies:
            for candy in row:
                self.sprites.add(candy)

    def swap(self, pos1, pos2):
        """Swap two adjacent candies."""
        (r1, c1), (r2, c2) = pos1, pos2
        if abs(r1 - r2) + abs(c1 - c2) != 1:
            return  # Not adjacent

        # Swap grid values
        self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]

        # Swap candy types and images
        c1_obj = self.candies[r1][c1]
        c2_obj = self.candies[r2][c2]
        c1_obj.type, c2_obj.type = c2_obj.type, c1_obj.type
        c1_obj.image = c1_obj.make_image()
        c2_obj.image = c2_obj.make_image()

        # Check matches
        matched = self.find_matches()
        if not matched:
            # Revert if no match
            self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]
            c1_obj.type, c2_obj.type = c2_obj.type, c1_obj.type
            c1_obj.image = c1_obj.make_image()
            c2_obj.image = c2_obj.make_image()

    def find_matches(self):
        """Find matches of 3+ candies horizontally or vertically."""
        matched = set()
        # Horizontal
        for r in range(ROWS):
            for c in range(COLS - 2):
                if self.grid[r][c] == self.grid[r][c + 1] == self.grid[r][c + 2]:
                    matched.update({(r, c), (r, c + 1), (r, c + 2)})
        # Vertical
        for c in range(COLS):
            for r in range(ROWS - 2):
                if self.grid[r][c] == self.grid[r + 1][c] == self.grid[r + 2][c]:
                    matched.update({(r, c), (r + 1, c), (r + 2, c)})
        # Replace matched candies
        for r, c in matched:
            new_type = random.randint(0, 11)
            self.grid[r][c] = new_type
            candy_obj = self.candies[r][c]
            candy_obj.type = new_type
            candy_obj.image = candy_obj.make_image()
        return matched


# =============================================================
# GAME SETUP
# =============================================================
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy Crush - Optimized Lesson 2")
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

    screen.fill((30, 30, 30))
    board.sprites.draw(screen)

    # Highlight selected candy
    if selected:
        rect = pygame.Rect(selected[1] * CELL_SIZE + 2, selected[0] * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4)
        pygame.draw.rect(screen, (255, 255, 255), rect, 3)

    pygame.display.flip()

pygame.quit()
