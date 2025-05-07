def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    row_zero = [i for i in range(rows) if all(grid[i][j]==0 for j in range(cols))]
    col_zero = [j for j in range(cols) if all(grid[i][j]==0 for i in range(rows))]
    dr1,dc1 = 1,2
    dr2,dc2 = 2,2
    seg_rows = [(row_zero[k]+1, row_zero[k+1]-1) for k in range(len(row_zero)-1)]
    seg_cols = [(col_zero[k]+1, col_zero[k+1]-1) for k in range(len(col_zero)-1)]
    h = seg_rows[0][1] - seg_rows[0][0] + 1
    w = seg_cols[0][1] - seg_cols[0][0] + 1
    vals1 = {}
    vals2 = {}
    for i,(r0,_r1) in enumerate(seg_rows):
        for j,(c0,_c1) in enumerate(seg_cols):
            v1 = grid[r0+dr1][c0+dc1]
            v2 = grid[r0+dr2][c0+dc2]
            vals1[v1] = vals1.get(v1,0)+1
            vals2[v2] = vals2.get(v2,0)+1
    default1 = max(vals1, key=lambda x: vals1[x])
    default2 = max(vals2, key=lambda x: vals2[x])
    out = [row[:] for row in grid]
    # propagate horizontal anomalies at dr1,dc1
    base_r1 = seg_rows[0][0] + dr1
    for j,(c0,_c1) in enumerate(seg_cols):
        base_c1 = c0 + dc1
        v = grid[base_r1][base_c1]
        if v!=default1:
            for i,(r0,_r1) in enumerate(seg_rows):
                out[r0+dr1][c0+dc1] = v
    # propagate vertical anomalies at dr2,dc2
    base_c2 = seg_cols[0][0] + dc2
    for i,(r0,_r1) in enumerate(seg_rows):
        base_r2 = r0 + dr2
        v = grid[base_r2][base_c2]
        if v!=default2:
            for j,(c0,_c1) in enumerate(seg_cols):
                out[r0+dr2][c0+dc2] = v
    return out