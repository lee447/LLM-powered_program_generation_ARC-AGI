from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def fill_ones(grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 0:
            return
        grid[r][c] = 1
        fill_ones(grid, r + 1, c)
        fill_ones(grid, r - 1, c)
        fill_ones(grid, r, c + 1)
        fill_ones(grid, r, c - 1)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fill_ones(grid, r, c)

    return grid