import numpy as np

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
            A = np.array([[grid[r0+dr][c0+dc] for c0,_ in seg_cols] for r0,_ in seg_rows])
            flat = A.flatten()
            if len(set(flat)) <= 1:
                continue
            vals, counts = np.unique(flat, return_counts=True)
            default = vals[np.argmax(counts)]
            mask = (A != default)
            if not mask.any() or mask.all():
                continue
            rows_idx, cols_idx = np.where(mask)
            if len(set(rows_idx)) == 1:
                i0 = rows_idx[0]
                val = A[i0, cols_idx[0]]
                for j in range(C):
                    out[seg_rows[i0][0]+dr][seg_cols[j][0]+dc] = val
            if len(set(cols_idx)) == 1:
                j0 = cols_idx[0]
                val = A[rows_idx[0], j0]
                for i in range(R):
                    out[seg_rows[i][0]+dr][seg_cols[j0][0]+dc] = val
    return out