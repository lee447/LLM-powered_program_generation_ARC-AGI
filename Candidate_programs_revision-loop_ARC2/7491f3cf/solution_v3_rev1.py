from collections import Counter
def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    cnt = Counter(c for row in grid for c in row if c != border)
    fg, hole = None, None
    for col, pts in sorted(((col, []) for col in cnt), key=lambda x: -cnt[x[0]]):
        pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == col]
        dr = {c - r for r, c in pts}
        if len(dr) == 1 and len(pts) > 1:
            hole = col
            break
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == hole]
    rs = [r for r, _ in pts]; cs = [c for _, c in pts]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    diag = {(r - r0, c - c0) for r, c in pts}
    anti = {(r, W - 1 - c) for r, c in diag}
    bg = Counter(c for row in grid for c in row if c not in (border, hole)).most_common(1)[0][0]
    for co in range(c1 + 1, w - W + 2):
        ok = True
        for dr, dc in anti:
            r, c = r0 + dr, co + dc
            if not (0 <= r < h and 0 <= c < w and grid[r][c] == bg):
                ok = False; break
        if ok:
            for dr, dc in anti:
                grid[r0 + dr][co + dc] = hole
            break
    return grid