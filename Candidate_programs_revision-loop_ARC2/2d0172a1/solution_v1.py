def solve(grid):
    H = len(grid)
    W = len(grid[0])
    cnt = {}
    for r in grid:
        for v in r:
            cnt[v] = cnt.get(v, 0) + 1
    bg = max(cnt, key=lambda k: cnt[k])
    best = None
    for r1 in range(H):
        for r2 in range(r1 + 2, H):
            for c1 in range(W):
                for c2 in range(c1 + 2, W):
                    c = grid[r1][c1]
                    if c == bg:
                        continue
                    ok = True
                    for x in range(c1, c2 + 1):
                        if grid[r1][x] != c or grid[r2][x] != c:
                            ok = False
                            break
                    if not ok:
                        continue
                    for y in range(r1, r2 + 1):
                        if grid[y][c1] != c or grid[y][c2] != c:
                            ok = False
                            break
                    if not ok:
                        continue
                    area = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if best is None or area > best[0]:
                        best = (area, r1, r2, c1, c2)
    if best is None:
        return grid
    _, r1, r2, c1, c2 = best
    return [row[c1:c2+1] for row in grid[r1:r2+1]]