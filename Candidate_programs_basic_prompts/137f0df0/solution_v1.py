def solve(grid):
    H = len(grid)
    W = len(grid[0])
    block_row_segments = []
    in_seg = False
    for r in range(H):
        if any(grid[r][c] != 0 for c in range(W)):
            if not in_seg:
                start = r
                in_seg = True
        else:
            if in_seg:
                block_row_segments.append((start, r - 1))
                in_seg = False
    if in_seg:
        block_row_segments.append((start, H - 1))
    block_col_segments = []
    in_seg = False
    for c in range(W):
        if any(grid[r][c] != 0 for r in range(H)):
            if not in_seg:
                start = c
                in_seg = True
        else:
            if in_seg:
                block_col_segments.append((start, c - 1))
                in_seg = False
    if in_seg:
        block_col_segments.append((start, W - 1))
    internal_sep_rows = []
    for i in range(len(block_row_segments) - 1):
        a = block_row_segments[i][1] + 1
        b = block_row_segments[i + 1][0] - 1
        internal_sep_rows.extend(range(a, b + 1))
    border_sep_rows = list(range(0, block_row_segments[0][0])) + list(range(block_row_segments[-1][1] + 1, H))
    internal_sep_cols = []
    for i in range(len(block_col_segments) - 1):
        a = block_col_segments[i][1] + 1
        b = block_col_segments[i + 1][0] - 1
        internal_sep_cols.extend(range(a, b + 1))
    border_sep_cols = list(range(0, block_col_segments[0][0])) + list(range(block_col_segments[-1][1] + 1, W))
    out = [list(row) for row in grid]
    bs_cols = set(border_sep_cols)
    bs_rows = set(border_sep_rows)
    is_cols = set(internal_sep_cols)
    is_rows = set(internal_sep_rows)
    for r in is_rows:
        for c in range(W):
            if c not in bs_cols:
                out[r][c] = 2
    for c in is_cols:
        for r in range(H):
            if r not in bs_rows:
                out[r][c] = 2
    for r in bs_rows:
        for c in is_cols:
            out[r][c] = 1
    for c in bs_cols:
        for r in is_rows:
            out[r][c] = 1
    return out