def solve(grid):
    R, C = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    row_col = [any(grid[r][c] != 0 for c in range(C)) for r in range(R)]
    col_col = [any(grid[r][c] != 0 for r in range(R)) for c in range(C)]
    row_segments = []
    r = 0
    while r < R:
        if row_col[r]:
            start = r
            while r + 1 < R and row_col[r + 1]:
                r += 1
            row_segments.append((start, r))
        r += 1
    col_segments = []
    c = 0
    while c < C:
        if col_col[c]:
            start = c
            while c + 1 < C and col_col[c + 1]:
                c += 1
            col_segments.append((start, c))
        c += 1
    internal_blank_rows = []
    for i in range(len(row_segments) - 1):
        for rr in range(row_segments[i][1] + 1, row_segments[i + 1][0]):
            internal_blank_rows.append(rr)
    internal_blank_cols = []
    for i in range(len(col_segments) - 1):
        for cc in range(col_segments[i][1] + 1, col_segments[i + 1][0]):
            internal_blank_cols.append(cc)
    row_min, row_max = row_segments[0][0], row_segments[-1][1]
    col_min, col_max = col_segments[0][0], col_segments[-1][1]
    for rr in internal_blank_rows:
        for c in range(C):
            out[rr][c] = 2 if col_min <= c <= col_max else 1
    for cc in internal_blank_cols:
        for r in range(R):
            out[r][cc] = 2 if row_min <= r <= row_max else 1
    return out