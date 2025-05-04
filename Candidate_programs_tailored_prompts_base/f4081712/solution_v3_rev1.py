from collections import Counter

def solve(grid):
    n, m = len(grid), len(grid[0])
    border = []
    for j in range(m):
        border.append(grid[0][j]); border.append(grid[n-1][j])
    for i in range(n):
        border.append(grid[i][0]); border.append(grid[i][m-1])
    bg = Counter(border).most_common(1)[0][0]
    row_counts = [len(set(row)) for row in grid]
    min_rc = min(row_counts)
    band_rows = [i for i,c in enumerate(row_counts) if c==min_rc]
    col_counts = [len(set(grid[i][j] for i in range(n))) for j in range(m)]
    min_cc = min(col_counts)
    band_cols = [j for j,c in enumerate(col_counts) if c==min_cc]
    if len(band_rows) > len(band_cols):
        r0, r1 = band_rows[0], band_rows[-1]
        above = r0
        below = n - r1 - 1
        if above < below:
            out = grid[:r0]
        else:
            out = grid[r1+1:]
    else:
        c0, c1 = band_cols[0], band_cols[-1]
        left = c0
        right = m - c1 - 1
        if left < right:
            out = [row[:c0] for row in grid]
        else:
            out = [row[c1+1:] for row in grid]
    return out