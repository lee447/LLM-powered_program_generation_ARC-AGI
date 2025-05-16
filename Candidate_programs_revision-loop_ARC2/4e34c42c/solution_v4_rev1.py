import numpy as np

def solve(grid):
    from collections import Counter
    H, W = len(grid), len(grid[0])
    cnt = Counter(x for row in grid for x in row)
    bg = cnt.most_common(1)[0][0]
    rows = [r for r in range(H) if any(grid[r][c] != bg for c in range(W))]
    segs = []
    for r in rows:
        if not segs or r > segs[-1][1] + 1:
            segs.append([r, r])
        else:
            segs[-1][1] = r
    heights = [b - a + 1 for a, b in segs]
    hcnt = Counter(heights)
    target_h = max(h for h, c in hcnt.items() if c >= 2)
    chosen = [seg for seg, h in zip(segs, heights) if h == target_h]
    chosen.sort(key=lambda x: x[0])
    top, bot = chosen
    r1, r2 = top
    r3, r4 = bot
    cols_top = [c for c in range(W) if any(grid[r][c] != bg for r in range(r1, r2+1))]
    cols_bot = [c for c in range(W) if any(grid[r][c] != bg for r in range(r3, r4+1))]
    h_top = r2 - r1 + 1
    h_bot = r4 - r3 + 1
    Hout = max(h_top, h_bot)
    pad_top = (Hout - h_top) // 2
    pad_bot = (Hout - h_bot) // 2
    out = []
    for i in range(Hout):
        row = []
        rb = r3 + i - pad_bot
        if r3 <= rb <= r4:
            row += [grid[rb][c] for c in cols_bot]
        else:
            row += [bg] * len(cols_bot)
        rt = r1 + i - pad_top
        if r1 <= rt <= r2:
            row += [grid[rt][c] for c in cols_top]
        else:
            row += [bg] * len(cols_top)
        out.append(row)
    return out