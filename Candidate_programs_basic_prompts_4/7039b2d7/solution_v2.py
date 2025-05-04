def solve(grid):
    M = len(grid)
    N = len(grid[0])
    rows_uniform = [i for i in range(M) if len(set(grid[i])) == 1]
    cols_uniform = [j for j in range(N) if len({grid[i][j] for i in range(M)}) == 1]
    row_seps = sorted(set([-1] + rows_uniform + [M]))
    col_seps = sorted(set([-1] + cols_uniform + [N]))
    row_ranges = [(row_seps[i] + 1, row_seps[i+1] - 1) for i in range(len(row_seps)-1) if row_seps[i] + 1 <= row_seps[i+1] - 1]
    col_ranges = [(col_seps[j] + 1, col_seps[j+1] - 1) for j in range(len(col_seps)-1) if col_seps[j] + 1 <= col_seps[j+1] - 1]
    out = []
    for r0, _ in row_ranges:
        row = []
        for c0, _ in col_ranges:
            row.append(grid[r0][c0])
        out.append(row)
    return out