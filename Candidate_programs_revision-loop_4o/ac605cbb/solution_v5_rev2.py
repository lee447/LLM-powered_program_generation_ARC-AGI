from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def fill_horizontal_line(r, c1, c2, color):
        for c in range(c1, c2 + 1):
            if grid[r][c] == 0:
                grid[r][c] = color

    def fill_vertical_line(c, r1, r2, color):
        for r in range(r1, r2 + 1):
            if grid[r][c] == 0:
                grid[r][c] = color

    def find_nonzero_positions():
        positions = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    positions.append((r, c, grid[r][c]))
        return positions

    positions = find_nonzero_positions()
    for r, c, color in positions:
        if r + 1 < len(grid) and grid[r + 1][c] == 0:
            fill_vertical_line(c, r, len(grid) - 1, color)
        if c + 1 < len(grid[0]) and grid[r][c + 1] == 0:
            fill_horizontal_line(r, c, len(grid[0]) - 1, color)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 0:
                color = grid[r][c]
                if r > 0 and grid[r-1][c] == 0:
                    fill_vertical_line(c, 0, r, color)
                if c > 0 and grid[r][c-1] == 0:
                    fill_horizontal_line(r, 0, c, color)

    return grid