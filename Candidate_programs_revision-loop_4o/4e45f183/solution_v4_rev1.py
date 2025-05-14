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

    def transpose(grid):
        return [list(row) for row in zip(*grid)]

    grid = transform_grid(grid)
    grid = transpose(grid)
    grid = transform_grid(grid)
    grid = transpose(grid)
    return grid