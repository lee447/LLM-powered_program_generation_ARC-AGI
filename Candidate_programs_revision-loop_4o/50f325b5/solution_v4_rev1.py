from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def fill_eights(grid, start_row, start_col):
        for row in range(start_row, len(grid)):
            for col in range(start_col, len(grid[0])):
                if grid[row][col] == 8:
                    grid[row][col] = 3
                elif grid[row][col] != 0:
                    return

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 8:
                fill_eights(grid, row, col)
    return grid