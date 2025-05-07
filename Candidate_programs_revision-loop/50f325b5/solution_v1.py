from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(0,1),(1,0)]
    out = [row[:] for row in grid]
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 3:
                for dy,dx in dirs:
                    run = [(y + k*dy, x + k*dx) for k in range(3)]
                    if all(0 <= yy < h and 0 <= xx < w and grid[yy][xx] == 3 for yy,xx in run):
                        for yy,xx in run:
                            out[yy][xx] = 8
    return out