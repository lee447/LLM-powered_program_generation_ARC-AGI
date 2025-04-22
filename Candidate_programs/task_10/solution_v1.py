from typing import List
import math

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    xs = [x for y in range(h) for x in range(w) if grid[y][x] != 0]
    ys = [y for y in range(h) for x in range(w) if grid[y][x] != 0]
    if not xs: return [row[:] for row in grid]
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(ys), max(ys)
    H = y1 - y0 + 1
    out = [row[:] for row in grid]
    for y in range(y0, y1+1):
        r = (y - y0) / (H - 1) if H > 1 else 0
        shift = int(round(math.sin(2*math.pi*r - math.pi/2)))
        for x in range(w):
            v = grid[y][x]
            if v != 0:
                nx = x + shift
                if 0 <= nx < w:
                    out[y][nx] = v
                out[y][x] = 0
    return out