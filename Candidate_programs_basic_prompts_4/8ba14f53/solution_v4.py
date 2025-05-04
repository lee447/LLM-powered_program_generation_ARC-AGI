from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    colors = sorted({c for row in grid for c in row if c != 0})
    info = []
    for c in colors:
        xs = [x for y in range(h) for x in range(w) if grid[y][x] == c]
        ys = [y for y in range(h) for x in range(w) if grid[y][x] == c]
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)
        z = 0
        for y in range(ymin+1, ymax):
            for x in range(xmin+1, xmax):
                if grid[y][x] == 0:
                    z += 1
        info.append((xmin, c, z))
    info.sort(key=lambda x: x[0])
    out = []
    for _, c, z in info:
        while z > 0 and len(out) < 3:
            k = min(z, 3)
            out.append([c]*k + [0]*(3-k))
            z -= k
    while len(out) < 3:
        out.append([0, 0, 0])
    return out