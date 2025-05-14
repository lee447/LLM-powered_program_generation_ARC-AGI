from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def fill_color(grid, x, y, target_color, new_color):
        if grid[x][y] != target_color:
            return
        grid[x][y] = new_color
        if x > 0:
            fill_color(grid, x - 1, y, target_color, new_color)
        if x < len(grid) - 1:
            fill_color(grid, x + 1, y, target_color, new_color)
        if y > 0:
            fill_color(grid, x, y - 1, target_color, new_color)
        if y < len(grid[0]) - 1:
            fill_color(grid, x, y + 1, target_color, new_color)

    def process_grid(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fill_color(grid, i, j, 1, 2)
                    return grid
        return grid

    return process_grid([row[:] for row in grid])