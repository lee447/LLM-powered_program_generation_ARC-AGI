def solve(grid):
    h, w = len(grid), len(grid[0])
    start = next(i for i in range(h) if any(grid[i][j] == 5 for j in range(w)))
    blocks = {}
    for r in range(start):
        for c in range(w):
            v = grid[r][c]
            if v not in (0, 5):
                if v not in blocks:
                    blocks[v] = [r, r, c, c]
                else:
                    b = blocks[v]
                    b[0], b[1] = min(b[0], r), max(b[1], r)
                    b[2], b[3] = min(b[2], c), max(b[3], c)
    bl = []
    for v, (r0, r1, c0, c1) in blocks.items():
        h0, w0 = r1 - r0 + 1, c1 - c0 + 1
        cr, cc = (r0 + r1) / 2, (c0 + c1) / 2
        bl.append((v, r0, c0, h0, w0, cr, cc))
    res = [row[:] for row in grid]
    for r in range(start, h):
        parity = (r - start) & 1
        for c in range(w):
            if grid[r][c] == 5:
                best = None
                bd = None
                bc = None
                for v, r0, c0, hh, ww, cr, cc in bl:
                    k = int(round((r - cr) / hh))
                    m = int(round((c - cc) / ww))
                    rt, ct = cr + k * hh, cc + m * ww
                    dr, dc = r - rt, c - ct
                    d = dr * dr + dc * dc
                    if bd is None or d < bd or (d == bd and (
                        (parity == 0 and ct < bc) or
                        (parity == 1 and ct > bc)
                    )):
                        bd, best, bc = d, v, ct
                res[r][c] = best
    return res