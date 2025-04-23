def solve(grid):
    H, W = len(grid), len(grid[0])
    r0 = c0 = None
    for r in range(H):
        for c in range(W - 2):
            if grid[r][c] == 8 and grid[r][c+1] == 8 and grid[r][c+2] == 8:
                r0, c0 = r, c
                break
        if r0 is not None:
            break
    center_r, center_c = r0, c0 + 1
    dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    best = None
    for dr, dc in dirs:
        step = 1
        rr, cc = center_r + dr, center_c + dc
        dist = None
        while 0 <= rr < H and 0 <= cc < W:
            if grid[rr][cc] != 0 and not (rr == r0 and c0 <= cc <= c0+2):
                dist = step
                break
            rr += dr; cc += dc; step += 1
        if dist is None:
            dist = step - 1
        fillable = 0
        for i in range(3):
            tr = r0 + dr * dist
            tc = c0 + i + dc * dist
            if 0 <= tr < H and 0 <= tc < W and grid[tr][tc] == 0:
                fillable += 1
        if fillable > 0:
            if best is None or dist < best[0]:
                best = (dist, dr, dc)
    if best is None:
        return grid
    dist, dr, dc = best
    out = [row[:] for row in grid]
    for i in range(3):
        tr = r0 + dr * dist
        tc = c0 + i + dc * dist
        if 0 <= tr < H and 0 <= tc < W and out[tr][tc] == 0:
            out[tr][tc] = 8
    return out