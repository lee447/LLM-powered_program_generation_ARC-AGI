def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    row_seps = [i for i in range(h) if all(v == 0 for v in grid[i])]
    col_seps = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    row_ranges = [(row_seps[k] + 1, row_seps[k+1] - 1) for k in range(len(row_seps)-1) if row_seps[k+1] - row_seps[k] > 1]
    col_starts = [col_seps[k] + 1 for k in range(len(col_seps)-1) if col_seps[k+1] - col_seps[k] > 1]
    for r0, r1 in row_ranges:
        row_idx = r0 + 2
        if row_idx > r1: continue
        if len(col_starts) < 2: continue
        anchor = grid[row_idx][col_starts[0] + 2]
        for c0 in col_starts[1:-1]:
            out[row_idx][c0 + 2] = anchor
    return out