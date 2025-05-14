from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def transform_row(row):
        new_row = row[:]
        for i in range(1, len(row) - 1):
            if row[i] != 0 and row[i - 1] == row[i + 1] and row[i - 1] != 0:
                new_row[i] = row[i - 1]
        return new_row

    def transform_grid(grid):
        transformed_grid = []
        for row in grid:
            transformed_grid.append(transform_row(row))
        return transformed_grid

    def fill_vertical(grid):
        for col in range(len(grid[0])):
            for row in range(1, len(grid) - 1):
                if grid[row][col] != 0 and grid[row - 1][col] == grid[row + 1][col] and grid[row - 1][col] != 0:
                    grid[row][col] = grid[row - 1][col]
        return grid

    grid = transform_grid(grid)
    grid = fill_vertical(grid)
    grid = transform_grid(grid)
    return grid