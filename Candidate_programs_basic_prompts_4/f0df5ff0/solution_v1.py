from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    ones = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == 1]
    for i, j in ones:
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and out[ni][nj] == 0:
                    out[ni][nj] = 1
    return out