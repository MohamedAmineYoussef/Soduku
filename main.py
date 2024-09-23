import pygame
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 540
CELL_SIZE = WIDTH // 9
LINE_COLOR = (0, 0, 0)  # black
BG_COLOR = (255, 255, 255)  # white
NUMBER_COLOR = (50, 50, 50)  # grey
HIGHLIGHT_COLOR = (0, 200, 0)  # green
FPS = 30

# Fonts
FONT = pygame.font.Font(None, 40)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")


def draw_grid():
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1  # separate each block with thicker lines
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)  # vertical lines
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)  # horizontal lines


def draw_numbers(grid):
    for r in range(9):  # going through rows
        for c in range(9):  # going through columns
            if grid[r][c] != 0:
                text = FONT.render(str(grid[r][c]), True, NUMBER_COLOR)
                screen.blit(text, (c * CELL_SIZE + 20, r * CELL_SIZE + 15))


def highlight_cell(r, c, color):
    pygame.draw.rect(screen, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def verify_valid(grid, r, c, k):
    not_in_row = k not in grid[r]
    not_in_col = all(k != grid[i][c] for i in range(9))
    not_in_square = all(
        k != grid[i][j] for i in range(r // 3 * 3, r // 3 * 3 + 3) for j in range(c // 3 * 3, c // 3 * 3 + 3))
    return not_in_row and not_in_col and not_in_square


def solve(grid, r=0, c=0):
    if r == 9:
        return True
    elif c == 9:
        return solve(grid, r + 1, 0)
    elif grid[r][c] != 0:
        return solve(grid, r, c + 1)
    else:
        for k in range(1, 10):
            if verify_valid(grid, r, c, k):
                grid[r][c] = k

                # Highlight the cell in green when a number is placed
                highlight_cell(r, c, (0, 255, 0))
                draw_grid()
                draw_numbers(grid)  # Draw numbers after highlighting
                pygame.display.update()
                time.sleep(0)  # Slow down to visualize

                if solve(grid, r, c + 1):
                    return True

                # If backtracking occurs, highlight the cell in red
                grid[r][c] = 0
                highlight_cell(r, c, (255, 0, 0))
                draw_grid()
                draw_numbers(grid)  # Draw numbers after highlighting
                pygame.display.update()
                time.sleep(0)  # Slow down to visualize

                # Reset to white after backtracking
                highlight_cell(r, c, BG_COLOR)
                draw_grid()
                draw_numbers(grid)  # Draw numbers after highlighting
                pygame.display.update()

        return False


def main():
    grid = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    running = True
    screen.fill(BG_COLOR)
    draw_grid()
    draw_numbers(grid)
    pygame.display.update()

    clock = pygame.time.Clock()

    solve(grid)

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()