def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    row_counts = [sum(1 for c in range(w-1) if grid[r][c]==8 and grid[r][c+1]==8) for r in range(h)]
    col_counts = [sum(1 for r in range(h-1) if grid[r][c]==8 and grid[r+1][c]==8) for c in range(w)]
    stripes_r = [r for r, cnt in enumerate(row_counts) if cnt]
    stripes_c = [c for c, cnt in enumerate(col_counts) if cnt]
    nodes = [(r, c) for r in stripes_r for c in stripes_c if grid[r][c] == 6]
    from collections import defaultdict
    diag = defaultdict(list)
    for r, c in nodes:
        diag[r + c].append((r, c))
    for pts in diag.values():
        if len(pts) < 2:
            continue
        pts.sort()
        for (r1, c1), (r2, c2) in zip(pts, pts[1:]):
            r0, r1_ = min(r1, r2), max(r1, r2)
            c0, c1_ = min(c1, c2), max(c1, c2)
            for rr in range(r0, r1_ + 1):
                for cc in range(c0, c1_ + 1):
                    if grid[rr][cc] != 6:
                        out[rr][cc] = 4
    return out