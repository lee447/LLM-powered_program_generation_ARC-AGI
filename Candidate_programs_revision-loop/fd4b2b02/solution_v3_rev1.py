import math
def solve(grid):
    R, C = len(grid), len(grid[0])
    pts = [(i, j) for i in range(R) for j in range(C) if grid[i][j] != 0]
    if not pts:
        return [[0]*C for _ in range(R)]
    rows = [i for i,_ in pts]; cols = [j for _,j in pts]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    h = r1 - r0 + 1; w = c1 - c0 + 1
    C0 = grid[r0][c0]; D = 9 - C0
    T = h + w
    out = [[0]*C for _ in range(R)]
    for k in range(-R//T-1, R//T+2):
        i0 = r0 + k*T
        for di in range(h):
            for dj in range(w):
                i, j = i0+di, c0+dj
                if 0 <= i < R and 0 <= j < C:
                    out[i][j] = C0
    for base in (r0 - w, r0 + h):
        for k in range(-R//T-1, R//T+2):
            i0 = base + k*T
            for di in range(w):
                for dj in range(h):
                    for jb in (c0 - h, c0 + w):
                        i, j = i0+di, jb+dj
                        if 0 <= i < R and 0 <= j < C:
                            out[i][j] = D
    return out