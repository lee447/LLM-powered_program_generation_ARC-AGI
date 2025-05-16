import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    start = next((i for i in range(h) if any(v == 5 for v in grid[i])), h)
    blocks = {}
    for r in range(start):
        for c in range(w):
            v = grid[r][c]
            if v not in (0, 5):
                if v not in blocks:
                    blocks[v] = [r, r, c, c]
                else:
                    b = blocks[v]
                    b[0] = min(b[0], r)
                    b[1] = max(b[1], r)
                    b[2] = min(b[2], c)
                    b[3] = max(b[3], c)
    bl = []
    for v, (r0, r1, c0, c1) in blocks.items():
        h0, w0 = r1 - r0 + 1, c1 - c0 + 1
        cr, cc = (r0 + r1) / 2, (c0 + c1) / 2
        bl.append((v, h0, w0, cr, cc))
    res = [row[:] for row in grid]
    for r in range(start, h):
        for c in range(w):
            if grid[r][c] == 5:
                best = None
                bd = None
                for v, hh, ww, cr, cc in bl:
                    k = int(round((r - cr) / hh))
                    m = int(round((c - cc) / ww))
                    dr = r - (cr + k * hh)
                    dc = c - (cc + m * ww)
                    d = dr * dr + dc * dc
                    if bd is None or d < bd:
                        bd = d
                        best = v
                res[r][c] = best
    return res