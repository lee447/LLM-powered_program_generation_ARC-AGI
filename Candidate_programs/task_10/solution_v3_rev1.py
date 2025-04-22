from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    xs = [x for y in range(h) for x in range(w) if grid[y][x] != 0]
    ys = [y for y in range(h) for x in range(w) if grid[y][x] != 0]
    if not xs:
        return [row[:] for row in grid]
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(ys), max(ys)
    color = None
    for y in range(y0, y1+1):
        for x in range(x0, x1+1):
            if grid[y][x] != 0:
                color = grid[y][x]
                break
        if color is not None:
            break
    base = [0, -1, 0, 1]
    p = color // 2 - 1
    out = [[0]*w for _ in range(h)]
    for y in range(y0, y1+1):
        d = y - y0
        shift = base[(d + p) % 4]
        for x in range(x0, x1+1):
            v = grid[y][x]
            if v:
                out[y][x+shift] = v
    return out