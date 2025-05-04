def solve(grid):
    h, w = len(grid), len(grid[0])
    th, bh, lh, rh = h, -1, w, -1
    sixes = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 3:
                th = min(th, y)
                bh = max(bh, y)
                lh = min(lh, x)
                rh = max(rh, x)
            elif grid[y][x] == 6:
                sixes.append((y, x))
    left_blk = [x for y, x in sixes if th <= y <= bh and x < lh]
    right_blk = [x for y, x in sixes if th <= y <= bh and x > rh]
    up_blk = [y for y, x in sixes if lh <= x <= rh and y < th]
    down_blk = [y for y, x in sixes if lh <= x <= rh and y > bh]
    nl, nr, nt, nb = lh, rh, th, bh
    if left_blk: nl = max(left_blk) + 1
    if right_blk: nr = min(right_blk) - 1
    if up_blk: nt = max(up_blk) + 1
    if down_blk: nb = min(down_blk) - 1
    out = [row[:] for row in grid]
    for x in range(nl, nr + 1):
        out[nt][x] = 3
        out[nb][x] = 3
    for y in range(nt, nb + 1):
        out[y][nl] = 3
        out[y][nr] = 3
    return out