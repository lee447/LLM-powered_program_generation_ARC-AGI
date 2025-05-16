import math
def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    rings = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                c = grid[i][j]
                pts = [(i, j)]
                seen[i][j] = True
                for k in range(len(pts)):
                    y, x = pts[k]
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx] == c:
                            seen[ny][nx] = True
                            pts.append((ny, nx))
                if len(pts) == 12:
                    ys = [p[0] for p in pts]
                    xs = [p[1] for p in pts]
                    rings.append((min(ys), min(xs), c))
    rings.sort(key=lambda t:(t[0], t[1]))
    n = len(rings)
    if n == 0:
        return []
    C = 2
    R = (n + C - 1)//C
    out = [[0]*(4*C) for _ in range(4*R)]
    for idx, (_, _, c) in enumerate(rings):
        r, col = divmod(idx, C)
        y0, x0 = 4*r, 4*col
        for dy in range(4):
            for dx in range(4):
                if dy in (0,3) or dx in (0,3):
                    out[y0+dy][x0+dx] = c
    return out