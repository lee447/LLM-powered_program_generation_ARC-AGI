from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    # find target color (8 if present else the rarest non-background)
    if any(8 in row for row in grid):
        color = 8
    else:
        cnt = {}
        for r in range(h):
            for c in range(w):
                x = grid[r][c]
                cnt[x] = cnt.get(x, 0) + 1
        bg = max(cnt, key=lambda x: (cnt[x], -x))
        color = min((x for x in cnt if x != bg), key=lambda x: (cnt[x], x))
    # collect the shape cells
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
    if not pts:
        return out
    # find bounding box
    r0 = min(r for r, c in pts)
    r1 = max(r for r, c in pts)
    c0 = min(c for r, c in pts)
    c1 = max(c for r, c in pts)
    shape = {(r - r0, c - c0) for r, c in pts}
    sh_h = r1 - r0 + 1
    sh_w = c1 - c0 + 1
    # decide fill color
    fill = color
    # tile the shape down the grid by steps of sh_h+2, shifting right by sh_w+2 each time
    dr = sh_h + 2
    dc = sh_w + 2
    for i, row_off in enumerate(range(r0 % dr, h, dr)):
        col_off = (c0 + i * dc) % w
        for sr, sc in shape:
            rr = row_off + sr
            cc = col_off + sc
            if 0 <= rr < h and 0 <= cc < w:
                out[rr][cc] = fill
    return out