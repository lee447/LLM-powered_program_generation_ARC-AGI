import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    blocks = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                if v not in blocks:
                    blocks[v] = [r, r, c, c]
                else:
                    blocks[v][0] = min(blocks[v][0], r)
                    blocks[v][1] = max(blocks[v][1], r)
                    blocks[v][2] = min(blocks[v][2], c)
                    blocks[v][3] = max(blocks[v][3], c)
    items = sorted(blocks.items(), key=lambda x: (x[1][0], x[1][2]))
    newpos = {}
    for v, (r0, r1, c0, c1) in items:
        width = c1 - c0 + 1
        nc = c0
        for u, (ur0, ur1, uc0, uc1) in items:
            if uc0 < c0:
                if not (r1 < ur0 or r0 > ur1):
                    if nc <= uc1:
                        nc = uc1 + 1
        newpos[v] = (r0, nc)
    out = [[0] * w for _ in range(h)]
    for v, (r0, r1, c0, c1) in blocks.items():
        nr0, nc0 = newpos[v]
        for r in range(r0, r1 + 1):
            for c in range(c0, c1 + 1):
                if grid[r][c] == v:
                    out[r][nc0 + (c - c0)] = v
    return out