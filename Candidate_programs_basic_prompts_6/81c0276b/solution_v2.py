def solve(grid):
    n, m = len(grid), len(grid[0])
    row_seps = [i for i in range(n) if len(set(grid[i])) == 1 and grid[i][0] != 0]
    wall = grid[row_seps[0]][0]
    col_seps = [j for j in range(m) if all(grid[i][j] == wall for i in range(n))]
    rs = [-1] + sorted(row_seps) + [n]
    cs = [-1] + sorted(col_seps) + [m]
    row_segs = [(rs[i]+1, rs[i+1]) for i in range(len(rs)-1) if rs[i+1]-rs[i]-1 >= 2]
    col_segs = [(cs[j]+1, cs[j+1]) for j in range(len(cs)-1) if cs[j+1]-cs[j]-1 >= 2]
    cells = []
    for r0, r1 in row_segs:
        for c0, c1 in col_segs:
            cnt = {}
            for i in range(r0, r1):
                for j in range(c0, c1):
                    v = grid[i][j]
                    if v != 0 and v != wall:
                        cnt[v] = cnt.get(v, 0) + 1
            if cnt:
                cells.append(max(cnt, key=cnt.get))
    freq = {}
    for v in cells:
        freq[v] = freq.get(v, 0) + 1
    colors = sorted(freq.items(), key=lambda x: x[1])
    distinct = [c for c, _ in colors]
    cols = len(col_segs)
    out = [[0]*cols for _ in distinct]
    for i, c in enumerate(distinct):
        for j in range(min(freq[c], cols)):
            out[i][j] = c
    return out