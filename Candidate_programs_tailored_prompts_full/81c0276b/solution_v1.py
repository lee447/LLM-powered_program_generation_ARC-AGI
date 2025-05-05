def solve(grid):
    R = len(grid)
    C = len(grid[0]) if R>0 else 0
    sep_rows = []
    for r in range(R):
        v = grid[r][0]
        if v!=0 and all(grid[r][c]==v for c in range(C)):
            sep_rows.append(r)
    sep_cols = []
    for c in range(C):
        v = grid[0][c]
        if v!=0 and all(grid[r][c]==v for r in range(R)):
            sep_cols.append(c)
    sep_rows.sort()
    sep_cols.sort()
    diffs_r = [sep_rows[i+1]-sep_rows[i] for i in range(len(sep_rows)-1)]
    diffs_c = [sep_cols[i+1]-sep_cols[i] for i in range(len(sep_cols)-1)]
    region_h = min(diffs_r)-1 if diffs_r else 0
    region_w = min(diffs_c)-1 if diffs_c else 0
    row_starts = [0] + [r+1 for r in sep_rows]
    col_starts = [0] + [c+1 for c in sep_cols]
    res = []
    for rs in row_starts:
        if rs+region_h>R: break
        row = []
        for cs in col_starts:
            if cs+region_w>C: break
            color = 0
            for i in range(rs, rs+region_h-1):
                for j in range(cs, cs+region_w-1):
                    v = grid[i][j]
                    if v!=0 and (not any(i==sr for sr in sep_rows)) and (not any(j==sc for sc in sep_cols)):
                        if grid[i][j]==grid[i+1][j]==grid[i][j+1]==grid[i+1][j+1]:
                            color = v
                            break
                if color: break
            row.append(color)
        res.append(row)
    return res