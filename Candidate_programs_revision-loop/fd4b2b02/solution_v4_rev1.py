import numpy as np

def solve(grid):
    R, C = len(grid), len(grid[0])
    pts = [(r, c) for r in range(R) for c in range(C) if grid[r][c] != 0]
    if not pts:
        return [[0]*C for _ in range(R)]
    rs, cs = zip(*pts)
    r0, c0 = min(rs), min(cs)
    h, w = max(rs)-r0+1, max(cs)-c0+1
    color = grid[r0][c0]
    other = 6 if color==3 else 3
    shp = [(r-r0, c-c0) for r,c in pts]
    rot = [(c-c0, h-1-(r-r0)) for r,c in pts]
    out = [[0]*C for _ in range(R)]
    rows = [0, r0, 2*r0]
    cols = [0, c0, 2*c0]
    for i in range(3):
        for j in range(3):
            if (i==1 and j==1) or ((i+j)%2==0):
                col, offs = color, shp
            else:
                col, offs = other, rot
            rr, cc = rows[i], cols[j]
            for dr, dc in offs:
                r, c = rr+dr, cc+dc
                if 0<=r<R and 0<=c<C:
                    out[r][c] = col
    return out