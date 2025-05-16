def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    pts = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != bg:
                pts.setdefault(v, []).append((r, c))
    out = [row[:] for row in grid]
    for v, ps in pts.items():
        rows = sorted(set(r for r, _ in ps))
        r0 = min(rows)
        if r0 - 5 >= 0:
            row_pts = sorted(c for r, c in ps if r == r0)
            n = len(row_pts)
            for i, c in enumerate(row_pts):
                nr, nc = r0 - 5, c
                if 0 <= nr < h and 0 <= nc < w:
                    if n % 2 == 1 and i == n//2:
                        out[nr][nc] = 1
                    elif i < n//2 + n%2:
                        out[nr][nc] = v
    return out