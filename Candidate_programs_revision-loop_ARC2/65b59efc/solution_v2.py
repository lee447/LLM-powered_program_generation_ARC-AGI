def solve(grid):
    n, m = len(grid), len(grid[0])
    fence = max(set(x for row in grid for x in row), key=lambda x: sum(r.count(x) for r in grid))
    rows = [i for i in range(n) if sum(1 for v in grid[i] if v == fence) > m//2]
    cols = [j for j in range(m) if sum(1 for i in range(n) if grid[i][j] == fence) > n//2]
    rs = [0] + [r+1 for r in rows] + [n+1]
    cs = [0] + [c+1 for c in cols] + [m+1]
    bh = rs[1] - rs[0] - 1
    bw = cs[1] - cs[0] - 1
    R = len(rs)-1
    C = len(cs)-1
    out = [[0]*(bw*C) for _ in range(bh*R)]
    for br in range(R):
        for bc in range(C):
            r0 = rs[br]
            c0 = cs[bc]
            color = 0
            cnt = {}
            for i in range(r0, min(r0+bh, n)):
                for j in range(c0, min(c0+bw, m)):
                    v = grid[i][j]
                    if v != 0 and v != fence:
                        cnt[v] = cnt.get(v,0)+1
            if cnt: color = max(cnt, key=cnt.get)
            for i in range(bh):
                for j in range(bw):
                    out[br*bh+i][bc*bw+j] = color
    return out