from collections import Counter

def solve(grid):
    rows, cols = len(grid), len(grid[0])
    row_zero = [i for i in range(rows) if all(grid[i][j]==0 for j in range(cols))]
    col_zero = [j for j in range(cols) if all(grid[i][j]==0 for i in range(rows))]
    seg_rows = [(row_zero[k]+1, row_zero[k+1]-1) for k in range(len(row_zero)-1)]
    seg_cols = [(col_zero[k]+1, col_zero[k+1]-1) for k in range(len(col_zero)-1)]
    R, C = len(seg_rows), len(seg_cols)
    h = seg_rows[0][1] - seg_rows[0][0] + 1
    w = seg_cols[0][1] - seg_cols[0][0] + 1
    out = [row[:] for row in grid]
    for dr in range(h):
        for dc in range(w):
            vals = []
            for i in range(R):
                for j in range(C):
                    vals.append(grid[seg_rows[i][0]+dr][seg_cols[j][0]+dc])
            mode = Counter(vals).most_common(1)[0][0]
            for i in range(R):
                for j in range(C):
                    out[seg_rows[i][0]+dr][seg_cols[j][0]+dc] = mode
    return out