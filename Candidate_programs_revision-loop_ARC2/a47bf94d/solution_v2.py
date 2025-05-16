from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for i in range(h-2):
        for j in range(w-2):
            c = grid[i][j]
            if c != 0 and all(grid[i+di][j+dj] == c for di in range(3) for dj in range(3)):
                for di in range(3):
                    for dj in range(3):
                        out[i+di][j+dj] = 0
                out[i][j+1]   = c
                out[i+1][j]   = c
                out[i+1][j+2] = c
                out[i+2][j+1] = c
    return out