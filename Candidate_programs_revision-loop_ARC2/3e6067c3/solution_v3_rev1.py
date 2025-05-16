import numpy as np
def solve(grid):
    h, w = len(grid), len(grid[0])
    bands = []
    for i in range(h):
        if any(grid[i][j] == 1 for j in range(w)):
            if not bands or i > bands[-1][1] + 1:
                bands.append([i, i])
            else:
                bands[-1][1] = i
    blocks = []
    for r0, r1 in bands:
        walls = sorted([c for c in range(w) if all(grid[r][c] == 1 for r in range(r0, r1 + 1))])
        pairs = [(walls[i], walls[i+1]) for i in range(0, len(walls), 2)]
        row = r0 + 1
        vals = [grid[row][c0+1] for c0, _ in pairs]
        blocks.append((pairs, vals))
    out = [list(r) for r in grid]
    for i in range(len(bands) - 1):
        top_end = bands[i][1]
        bot_start = bands[i+1][0]
        r0, r1 = top_end + 1, bot_start - 1
        if r0 > r1: continue
        height = r1 - r0 + 1
        pairs0, vals0 = blocks[i]
        pairs1, vals1 = blocks[i+1]
        if height > 1:
            ps = [0, len(pairs0)-1]
        else:
            ps = list(range(1, len(pairs0)))
        for p in ps:
            if p >= len(pairs0): continue
            c0, c1 = pairs0[p]
            if height > 1:
                col = vals0[p]
            else:
                if p % 2 == 1:
                    col = vals0[p]
                else:
                    col = vals1[p] if p < len(vals1) else vals1[-1]
            for r in range(r0, r1+1):
                for c in range(c0+1, c1):
                    out[r][c] = col
    return out