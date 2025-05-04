def solve(grid):
    H, W = len(grid), len(grid[0])
    cols = set()
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v not in (0,1,4):
                cols.add(v)
    fill = cols.pop() if cols else 0
    res = [row[:] for row in grid]
    patterns = [
        [(-1, -1), (-1,  1)],
        [( 1, -1), ( 1,  1)],
        [(-1, -1), ( 1, -1)],
        [(-1,  1), ( 1,  1)]
    ]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 1:
                for arms in patterns:
                    pts = [(i, j)]
                    ok = True
                    for dy, dx in arms:
                        y, x = i + dy, j + dx
                        if not (0 <= y < H and 0 <= x < W and grid[y][x] == 1):
                            ok = False
                            break
                        pts.append((y, x))
                    if ok:
                        for y, x in pts:
                            res[y][x] = fill
    return res