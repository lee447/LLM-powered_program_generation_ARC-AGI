from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def process_row(row):
        new_row = [0] * len(row)
        for i in range(1, len(row) - 1):
            if row[i] != 0 and row[i - 1] == 0 and row[i + 1] == 0:
                new_row[i] = 0
            else:
                new_row[i] = row[i]
        return new_row

    def process_grid(grid):
        new_grid = []
        for row in grid:
            new_grid.append(process_row(row))
        return new_grid

    return process_grid(grid)