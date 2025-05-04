import math
def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    def inb(x, y):
        return 0 <= x < h and 0 <= y < w
    for color in range(2, 10):
        pts = [(i, j) for i in range(h) for j in range(w) if res[i][j] == color]
        if len(pts) != 2:
            continue
        (x1, y1), (x2, y2) = pts
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        new = set()
        for x, y in pts:
            for k in (1, 3):
                if k == 1:
                    dx = -(y - cy)
                    dy =  (x - cx)
                else:
                    dx =  (y - cy)
                    dy = -(x - cx)
                nx = cx + dx
                ny = cy + dy
                if abs(nx - round(nx)) < 1e-6 and abs(ny - round(ny)) < 1e-6:
                    xi, yi = int(round(nx)), int(round(ny))
                    if inb(xi, yi) and res[xi][yi] == 1:
                        new.add((xi, yi))
        for xi, yi in new:
            res[xi][yi] = color
    return res