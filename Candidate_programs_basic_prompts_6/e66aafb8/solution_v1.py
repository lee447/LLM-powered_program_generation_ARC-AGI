def solve(grid):
    H, W = len(grid), len(grid[0])
    rmin = H; rmax = -1; cmin = W; cmax = -1
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 0:
                if r < rmin: rmin = r
                if r > rmax: rmax = r
                if c < cmin: cmin = c
                if c > cmax: cmax = c
    h = rmax - rmin + 1
    w = cmax - cmin + 1
    counts = {}
    for r0 in range(H - h + 1):
        for c0 in range(W - w + 1):
            block = []
            ok = True
            for i in range(h):
                row = grid[r0 + i][c0:c0 + w]
                if any(v == 0 for v in row):
                    ok = False
                    break
                block.append(tuple(row))
            if not ok: continue
            tpl = tuple(block)
            counts[tpl] = counts.get(tpl, 0) + 1
    best = max(counts, key=counts.get)
    return [list(row) for row in best]