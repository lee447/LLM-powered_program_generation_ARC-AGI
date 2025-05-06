def solve(grid):
    h, w = len(grid), len(grid[0])
    centers = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 5]
    (r1, c1), (r2, c2) = centers if centers[0][0] < centers[1][0] else centers[::-1]
    dr = 1 if r2 > r1 else -1
    dc = 1 if c2 > c1 else -1
    exit1 = (r1 + dr, c1)
    exit2 = (r2, c1)
    exit3 = (r2, c2 - dc)
    path = set()
    r, c = exit1
    while True:
        path.add((r, c))
        if r == exit2[0]:
            break
        r += dr
    r, c = exit2
    while True:
        path.add((r, c))
        if c == exit3[1]:
            break
        c += dc
    rs = [r for r, _ in path]
    cs = [c for _, c in path]
    rmin, rmax = min(rs), max(rs)
    cmin, cmax = min(cs), max(cs)
    for i in range(rmin, rmax + 1):
        for j in range(cmin, cmax + 1):
            if grid[i][j] == 0:
                grid[i][j] = 4
    return grid