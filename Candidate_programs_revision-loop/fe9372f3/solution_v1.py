def solve(grid):
    m, n = len(grid), len(grid[0])
    coords = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2]
    from collections import Counter
    rc = Counter(i for i, _ in coords)
    if any(v == 3 for v in rc.values()):
        cr = next(r for r, v in rc.items() if v == 3)
        cs = sorted(j for i, j in coords if i == cr)
        cc = cs[1]
    else:
        ccnt = Counter(j for _, j in coords)
        cc = next(c for c, v in ccnt.items() if v == 3)
        rs = sorted(i for i, j in coords if j == cc)
        cr = rs[1]
    out = [[0]*n for _ in range(m)]
    for i, j in coords:
        out[i][j] = 2
    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        k = 1
        while True:
            i, j = cr+dr*k, cc+dc*k
            if not (0<=i<m and 0<=j<n): break
            if out[i][j] == 0:
                out[i][j] = 1
            k += 1
    seq = [8,8,4]
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        k = 1
        while True:
            i, j = cr+dr*k, cc+dc*k
            if not (0<=i<m and 0<=j<n): break
            if out[i][j] == 0 and k >= 2:
                out[i][j] = seq[(k-2) % 3]
            k += 1
    return out