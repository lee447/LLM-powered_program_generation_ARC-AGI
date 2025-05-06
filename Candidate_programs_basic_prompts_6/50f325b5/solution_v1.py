def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 8]
    if not pts:
        return grid
    minr = min(r for r, _ in pts)
    minc = min(c for _, c in pts)
    maxr = max(r for r, _ in pts)
    maxc = max(c for _, c in pts)
    shape = [(r - minr, c - minc) for r, c in pts]
    h, w = maxr - minr + 1, maxc - minc + 1
    for dr in range(0, H - h + 1, h):
        for dc in range(0, W - w + 1, w):
            if dr == minr and dc == minc:
                continue
            ok = True
            for so_r, so_c in shape:
                r, c = dr + so_r, dc + so_c
                if not (0 <= r < H and 0 <= c < W):
                    ok = False
                    break
            if not ok:
                continue
            for so_r, so_c in shape:
                r, c = dr + so_r, dc + so_c
                grid[r][c] = 8
    for dr in range(0, H - h + 1, h):
        for dc in range(0, W - w + 1, w):
            if dr == minr and dc == minc:
                continue
            ok = True
            for so_r, so_c in shape:
                r, c = dr + so_r, dc + so_c
                if not (0 <= r < H and 0 <= c < W):
                    ok = False
                    break
            if not ok:
                continue
            for so_r, so_c in shape:
                r, c = dr + so_r, dc + so_c
                grid[r][c] = 8
    return grid