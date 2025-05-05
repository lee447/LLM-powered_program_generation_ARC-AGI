def solve(grid):
    h, w = len(grid), len(grid[0])
    g = grid[2:h-2]
    g = [row[2:w-2] for row in g]
    zs = [i for i, row in enumerate(g) if 0 in row]
    zr0, zr1 = min(zs), max(zs)
    zc = [j for j in range(len(g[0])) if any(g[i][j] == 0 for i in zs)]
    zc0, zc1 = min(zc), max(zc)
    g2 = []
    for i, row in enumerate(g):
        if zr0 <= i <= zr1: continue
        g2.append([v for j, v in enumerate(row) if not (zc0 <= j <= zc1)])
    res = []
    for r in g2:
        if not res or r != res[-1]:
            res.append(r)
    stripe_w = zc1 - zc0 + 1
    half_w = len(res[0]) // 2
    out = [r[half_w:half_w+stripe_w] for r in res]
    return out[::-1]