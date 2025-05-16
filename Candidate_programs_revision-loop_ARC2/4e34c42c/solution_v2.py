def solve(grid):
    from collections import Counter, deque
    H, W = len(grid), len(grid[0])
    cnt = Counter(x for row in grid for x in row)
    bg = cnt.most_common(1)[0][0]
    # find non-background row segments
    rows = [r for r in range(H) if any(grid[r][c] != bg for c in range(W))]
    segs = []
    for r in rows:
        if not segs or r > segs[-1][1] + 1:
            segs.append([r, r])
        else:
            segs[-1][1] = r
    # choose top and bottom segments
    if bg == 8:
        top, bot = segs[0], segs[1]
    else:
        top, bot = segs[0], segs[-1]
    r1, r2 = top
    r3, r4 = bot
    # columns for top block: all cols where any row in [r1..r2] is non-bg
    cols_top = [c for c in range(W) if any(grid[r][c] != bg for r in range(r1, r2+1))]
    # columns for bottom block: all cols where any row in [r3..r4] is non-bg
    cols_bot = [c for c in range(W) if any(grid[r][c] != bg for r in range(r3, r4+1))]
    # pad both to same height
    h_top = r2 - r1 + 1
    h_bot = r4 - r3 + 1
    Hout = max(h_top, h_bot)
    pad_top_top = (Hout - h_top) // 2
    pad_bot_top = (Hout - h_bot) // 2
    out = []
    for i in range(Hout):
        row = []
        # bottom block rows
        rb = r3 + (i - pad_bot_top)
        if r3 <= rb <= r4:
            row += [grid[rb][c] for c in cols_bot]
        else:
            row += [bg] * len(cols_bot)
        # top block rows
        rt = r1 + (i - pad_top_top)
        if r1 <= rt <= r2:
            row += [grid[rt][c] for c in cols_top]
        else:
            row += [bg] * len(cols_top)
        out.append(row)
    return out