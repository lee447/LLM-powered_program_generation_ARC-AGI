def solve(grid):
    H, W = len(grid), len(grid[0])
    pts3 = [(r,c) for r in range(H) for c in range(W) if grid[r][c]==3]
    if not pts3:
        return grid
    t0 = min(r for r,c in pts3)
    b0 = max(r for r,c in pts3)
    l0 = min(c for r,c in pts3)
    r0 = max(c for r,c in pts3)
    pinks = [(r,c) for r in range(H) for c in range(W) if grid[r][c]==6]
    new_t, new_b, new_l, new_r = t0, b0, l0, r0
    # horizontal influencers
    Ph = [c for r,c in pinks if t0 <= r <= b0]
    if Ph:
        pmn, pmx = min(Ph), max(Ph)
        if pmn < l0:
            new_l = pmn + 1
        if pmx > r0:
            new_r = pmx - 1
    # vertical influencers
    Pv = [r for r,c in pinks if l0 <= c <= r0]
    if Pv:
        rmn, rmx = min(Pv), max(Pv)
        if rmn < t0:
            new_t = rmn + 1
        if rmx > b0:
            new_b = rmx - 1
    # clear old 3s
    out = [[grid[r][c] if grid[r][c]!=3 else 0 for c in range(W)] for r in range(H)]
    # draw new frame
    for c in range(new_l, new_r+1):
        out[new_t][c] = 3
        out[new_b][c] = 3
    for r in range(new_t, new_b+1):
        out[r][new_l] = 3
        out[r][new_r] = 3
    return out