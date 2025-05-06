from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    p = next(i for i in range(1, h) if grid[i] == grid[0])
    original = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if original[i][j] == 0:
                grid[i][j] = original[i % p][j % p]
    return grid