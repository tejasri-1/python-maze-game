import pygame
import random

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_WIDTH, CELL_HEIGHT = WIDTH // COLS, HEIGHT // ROWS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def generate_maze(grid, row, col):
    grid[row][col] = False
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)
    for d_row, d_col in directions:
        new_row, new_col = row + 2 * d_row, col + 2 * d_col
        if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col]:
            grid[row + d_row][col + d_col] = False
            generate_maze(grid, new_row, new_col)

def draw_grid(screen, grid):
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col]:
                pygame.draw.rect(screen, BLACK, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Random Maze Generation")

    grid = [[True for _ in range(COLS)] for _ in range(ROWS)]
    generate_maze(grid, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_grid(screen, grid)

    pygame.quit()

if __name__ == "__main__":
    main()
