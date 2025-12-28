import pygame
import random
import sys

# -------------------- CONFIG -------------------- #
ROWS, COLS = 8, 8
CANDY_SIZE = 60
PADDING = 5
SCREEN_WIDTH = COLS * CANDY_SIZE
SCREEN_HEIGHT = ROWS * CANDY_SIZE
FPS = 60

COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
    (128, 0, 128)   # Purple
]

# -------------------- CLASSES -------------------- #
class Candy:
    def __init__(self, row, col, color=None):
        self.row = row
        self.col = col
        self.color = color if color else random.choice(COLORS)

    def draw(self, surface):
        x = self.col * CANDY_SIZE + CANDY_SIZE // 2
        y = self.row * CANDY_SIZE + CANDY_SIZE // 2
        pygame.draw.circle(surface, self.color, (x, y), CANDY_SIZE // 2 - PADDING)

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Candy(r, c) for c in range(cols)] for r in range(rows)]

    def draw(self, surface):
        for row in self.grid:
            for candy in row:
                candy.draw(surface)

    def swap(self, pos1, pos2):
        r1, c1 = pos1
        r2, c2 = pos2
        self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]
        # Update their positions
        self.grid[r1][c1].row, self.grid[r1][c1].col = r1, c1
        self.grid[r2][c2].row, self.grid[r2][c2].col = r2, c2

    def find_matches(self):
        matched = set()
        # Check rows
        for r in range(self.rows):
            for c in range(self.cols - 2):
                if self.grid[r][c].color == self.grid[r][c+1].color == self.grid[r][c+2].color:
                    matched.update([(r, c), (r, c+1), (r, c+2)])
        # Check cols
        for c in range(self.cols):
            for r in range(self.rows - 2):
                if self.grid[r][c].color == self.grid[r+1][c].color == self.grid[r+2][c].color:
                    matched.update([(r, c), (r+1, c), (r+2, c)])
        return matched

    def remove_matches(self, matches):
        for (r, c) in matches:
            self.grid[r][c] = None

    def collapse(self):
        """ Make candies fall down and generate new ones """
        for c in range(self.cols):
            empty_rows = []
            for r in range(self.rows-1, -1, -1):
                if self.grid[r][c] is None:
                    empty_rows.append(r)
                elif empty_rows:
                    new_r = empty_rows.pop(0)
                    self.grid[new_r][c] = self.grid[r][c]
                    self.grid[new_r][c].row = new_r
                    self.grid[r][c] = None
                    empty_rows.append(r)
            # Fill top with new candies
            for r in empty_rows:
                self.grid[r][c] = Candy(r, c)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Candy Crush (Simplified)")
        self.clock = pygame.time.Clock()
        self.board = Board(ROWS, COLS)
        self.selected = None

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                row, col = my // CANDY_SIZE, mx // CANDY_SIZE
                if self.selected:
                    prev_r, prev_c = self.selected
                    # Only allow swap with adjacent cell
                    if abs(prev_r - row) + abs(prev_c - col) == 1:
                        self.board.swap((prev_r, prev_c), (row, col))
                    self.selected = None
                else:
                    self.selected = (row, col)

    def update(self):
        matches = self.board.find_matches()
        if matches:
            self.board.remove_matches(matches)
            self.board.collapse()

    def draw(self):
        self.screen.fill((50, 50, 50))
        self.board.draw(self.screen)
        pygame.display.flip()

# -------------------- MAIN -------------------- #
if __name__ == "__main__":
    Game().run()
