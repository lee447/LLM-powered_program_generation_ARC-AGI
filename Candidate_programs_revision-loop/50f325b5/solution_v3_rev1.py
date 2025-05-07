from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 3:
                for dy, dx in ((0, 1), (1, 0)):
                    y2, x2 = y + 2*dy, x + 2*dx
                    if 0 <= y2 < h and 0 <= x2 < w and all(grid[y + k*dy][x + k*dx] == 3 for k in range(3)):
                        yp, xp = y - dy, x - dx
                        y3, x3 = y + 3*dy, x + 3*dx
                        if not (0 <= yp < h and 0 <= xp < w and grid[yp][xp] == 3) and not (0 <= y3 < h and 0 <= x3 < w and grid[y3][x3] == 3):
                            for k in range(3):
                                out[y + k*dy][x + k*dx] = 8
    return out