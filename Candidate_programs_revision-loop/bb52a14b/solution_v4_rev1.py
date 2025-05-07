from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for i in range(h-2):
        for j in range(w-2):
            colors = set()
            count_nz = 0
            for di in range(3):
                for dj in range(3):
                    v = grid[i+di][j+dj]
                    if v != 0:
                        colors.add(v)
                        count_nz += 1
            if colors == {1, 8} and count_nz >= 4 and grid[i+1][j+1] != 0:
                for di in range(3):
                    for dj in range(3):
                        if out[i+di][j+dj] == 0:
                            out[i+di][j+dj] = 4
    return out