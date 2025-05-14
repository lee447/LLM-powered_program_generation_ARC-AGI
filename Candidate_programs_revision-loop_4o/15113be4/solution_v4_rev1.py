from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_color_change(grid):
        for row in grid:
            for i in range(len(row) - 1):
                if row[i] != row[i + 1] and row[i] != 4 and row[i + 1] != 4:
                    return row[i + 1]
        return None

    def apply_color_change(grid, color):
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] != 4:
                    grid[r][c] = (grid[r][c] + color) % 10
        return grid

    color_change = find_color_change(grid)
    if color_change is not None:
        return apply_color_change(grid, color_change)
    return grid