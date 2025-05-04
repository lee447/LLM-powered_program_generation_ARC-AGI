from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    clusters = [(i, j) for i in range(H-1) for j in range(W-1)
                if grid[i][j]==5 and grid[i+1][j]==5 and grid[i][j+1]==5 and grid[i+1][j+1]==5]
    if not clusters:
        return [row[:] for row in grid]
    rows = sorted({i for i,_ in clusters})
    cols = sorted({j for _,j in clusters})
    min_r, max_r = rows[0], rows[-1]+1
    min_c, max_c = cols[0], cols[-1]+1
    cluster_rows = set(r for r in rows for r in (r, r+1))
    cluster_cols = set(c for c in cols for c in (c, c+1))
    row_gap_rows = [i for i in range(min_r, max_r+1) if i not in cluster_rows]
    col_gap_cols = [j for j in range(min_c, max_c+1) if j not in cluster_cols]
    out = [row[:] for row in grid]
    for i in row_gap_rows:
        for j in range(min_c, max_c+1):
            if out[i][j]==0:
                out[i][j]=2
    for j in col_gap_cols:
        for i in range(min_r, max_r+1):
            if out[i][j]==0:
                out[i][j]=2
    for i in row_gap_rows:
        for j in range(0, min_c):
            if out[i][j]==0:
                out[i][j]=1
        for j in range(max_c+1, W):
            if out[i][j]==0:
                out[i][j]=1
    for j in col_gap_cols:
        for i in range(0, min_r):
            if out[i][j]==0:
                out[i][j]=1
        for i in range(max_r+1, H):
            if out[i][j]==0:
                out[i][j]=1
    return out