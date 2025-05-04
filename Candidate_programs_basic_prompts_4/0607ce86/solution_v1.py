def solve(grid):
    R = len(grid)
    C = len(grid[0])
    row_counts = [sum(1 for x in row if x != 0) for row in grid]
    max_row = max(row_counts)
    thr_row = max_row / 2.0
    rows = [i for i, c in enumerate(row_counts) if c >= thr_row]
    row_intervals = []
    if rows:
        s = p = rows[0]
        for i in rows[1:]:
            if i == p + 1:
                p = i
            else:
                row_intervals.append((s, p))
                s = p = i
        row_intervals.append((s, p))
    col_counts = [0] * C
    for i in rows:
        for j in range(C):
            if grid[i][j] != 0:
                col_counts[j] += 1
    max_col = max(col_counts)
    thr_col = max_col / 2.0
    cols = [j for j, c in enumerate(col_counts) if c >= thr_col]
    col_intervals = []
    if cols:
        s = p = cols[0]
        for j in cols[1:]:
            if j == p + 1:
                p = j
            else:
                col_intervals.append((s, p))
                s = p = j
        col_intervals.append((s, p))
    ref = {}
    for r1, r2 in row_intervals:
        patterns = {}
        for c1, c2 in col_intervals:
            pat = tuple(tuple(grid[i][j] for j in range(c1, c2 + 1)) for i in range(r1, r2 + 1))
            patterns[pat] = patterns.get(pat, 0) + 1
        ref[(r1, r2)] = max(patterns.items(), key=lambda x: x[1])[0]
    out = [[0] * C for _ in range(R)]
    for (r1, r2), pat in ref.items():
        h = r2 - r1 + 1
        w = len(pat[0])
        for c1, c2 in col_intervals:
            for di in range(h):
                for dj in range(w):
                    out[r1 + di][c1 + dj] = pat[di][dj]
    return out