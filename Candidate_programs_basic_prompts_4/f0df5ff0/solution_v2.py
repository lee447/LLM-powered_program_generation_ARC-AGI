from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    seeds = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 1]
    res = [row[:] for row in grid]
    for i, j in seeds:
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 0:
                    res[ni][nj] = 1
    return res