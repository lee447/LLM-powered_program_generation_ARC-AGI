def solve(grid):
    n = len(grid)
    m = len(grid[0])
    row_seps = {i for i, row in enumerate(grid) if len(set(row)) == 1}
    col_seps = {j for j in range(m) if len({grid[i][j] for i in range(n)}) == 1}
    rows = []
    rs = 0
    for i in range(n):
        if i in row_seps:
            if rs < i:
                rows.append((rs, i))
            rs = i + 1
    if rs < n:
        rows.append((rs, n))
    cols = []
    cs = 0
    for j in range(m):
        if j in col_seps:
            if cs < j:
                cols.append((cs, j))
            cs = j + 1
    if cs < m:
        cols.append((cs, m))
    out = [[0]*len(cols) for _ in rows]
    for i, (r0, r1) in enumerate(rows):
        for j, (c0, c1) in enumerate(cols):
            cnt = {}
            for r in range(r0, r1):
                for c in range(c0, c1):
                    v = grid[r][c]
                    cnt[v] = cnt.get(v, 0) + 1
            mv = max(cnt, key=cnt.get)
            out[i][j] = mv
    return out