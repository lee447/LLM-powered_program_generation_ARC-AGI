def solve(grid):
    h = len(grid)
    w = len(grid[0])
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    rs = sorted(r for r, _ in ones)
    cs = sorted(c for _, c in ones)
    pr = rs[len(rs) // 2]
    pc = cs[len(cs) // 2]
    template = [(r - pr, c - pc) for r, c in ones]
    max_dr = max(template, key=lambda x: abs(x[0]))[0]
    max_dc = max(template, key=lambda x: abs(x[1]))[1]
    if abs(max_dc) > abs(max_dr):
        orig = "right" if max_dc > 0 else "left"
    else:
        orig = "down" if max_dr > 0 else "up"
    cnt = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v not in (0, 1):
                cnt[v] = cnt.get(v, 0) + 1
    seeds = [(r, c, grid[r][c]) for r in range(h) for c in range(w)
             if grid[r][c] not in (0, 1) and cnt.get(grid[r][c], 0) == 1]
    out = [row[:] for row in grid]
    dirs = ["up", "right", "down", "left"]
    for sr, sc, v in seeds:
        tgt = "right" if v in (3, 6) else "down"
        ki = (dirs.index(tgt) - dirs.index(orig)) % 4
        for dr, dc in template:
            r0, c0 = dr, dc
            for _ in range(ki):
                r0, c0 = -c0, r0
            rr, cc = sr + r0, sc + c0
            if 0 <= rr < h and 0 <= cc < w:
                out[rr][cc] = v
    return out