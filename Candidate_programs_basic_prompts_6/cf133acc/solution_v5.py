def solve(grid):
    n = len(grid)
    m = len(grid[0])
    crosses = {}
    for i, row in enumerate(grid):
        pos = {}
        for j, v in enumerate(row):
            if v:
                pos.setdefault(v, []).append(j)
        for v, cols in pos.items():
            if len(cols) > 1:
                cols = sorted(cols)
                groups = [[cols[0]]]
                for c in cols[1:]:
                    if c == groups[-1][-1] + 1:
                        groups[-1].append(c)
                    else:
                        groups.append([c])
                if len(groups) == 2 and groups[1][0] - groups[0][-1] == 2:
                    c = groups[0][-1] + 1
                    crosses.setdefault(c, []).append((i, v, min(cols), max(cols)))
    out = [[0]*m for _ in range(n)]
    for c, lst in crosses.items():
        lst.sort(key=lambda x: x[0])
        hs = {v for _, v, *_ in lst}
        col_colors = {grid[i][c] for i in range(n) if grid[i][c] and grid[i][c] not in hs}
        V = col_colors.pop() if col_colors else None
        r_v = next((i for i in range(n) if V is not None and grid[i][c] == V), n)
        for r, v, lo, hi in lst:
            for j in range(lo, hi+1):
                out[r][j] = v
        for idx, (r, v, *_ ) in enumerate(lst):
            start = 0 if idx == 0 else lst[idx-1][0] + 1
            end = r - 1
            for i in range(start, end+1):
                out[i][c] = v
        last_r = lst[-1][0]
        if V is not None:
            for i in range(last_r+1, r_v):
                out[i][c] = V
            for i in range(r_v, n):
                out[i][c] = grid[i][c]
    return out