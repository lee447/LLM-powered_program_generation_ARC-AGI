from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    stripe_rows = [i for i in range(H) if len({grid[i][j] for j in range(W)})==1 and grid[i][0]!=0]
    stripe_cols = [j for j in range(W) if len({grid[i][j] for i in range(H)})==1 and grid[0][j]!=0]
    stripe_rows.sort()
    stripe_cols.sort()
    sc = grid[stripe_rows[0]][stripe_cols[0]]
    sr_ext = [-1] + stripe_rows + [H]
    sc_ext = [-1] + stripe_cols + [W]
    row_ranges = [range(sr_ext[k]+1, sr_ext[k+1]) for k in range(len(sr_ext)-1)]
    col_ranges = [range(sc_ext[k]+1, sc_ext[k+1]) for k in range(len(sc_ext)-1)]
    row_counts = [sum(1 for i in rr for j in range(W) if grid[i][j]!=0 and grid[i][j]!=sc) for rr in row_ranges]
    ru_sel = max(range(len(row_counts)), key=lambda k: row_counts[k])
    ru = row_ranges[ru_sel]
    col_counts = [sum(1 for i in ru for j in cr if grid[i][j]!=0 and grid[i][j]!=sc) for cr in col_ranges]
    src_cols = [k for k,c in enumerate(col_counts) if c>0]
    n_row_int = sum(1 for c in row_counts if c>0)
    n_col_int = len(src_cols)
    out = [row[:] for row in grid]
    # vertical mapping
    if n_col_int>1 and n_row_int==1 and ru_sel+1<len(row_ranges):
        s = sr_ext[ru_sel+1]
        dest_ru = row_ranges[ru_sel+1]
        # clear
        for i in dest_ru:
            for j_idx in src_cols:
                for j in col_ranges[j_idx]:
                    if out[i][j]!=0 and out[i][j]!=sc:
                        out[i][j]=0
        # copy
        for i in ru:
            for j_idx in src_cols:
                for j in col_ranges[j_idx]:
                    v = grid[i][j]
                    if v!=0 and v!=sc:
                        di = 2*s - i
                        out[di][j] = v
    # horizontal mapping
    elif n_row_int>1 and n_col_int==1 and src_cols[0]+1<len(col_ranges):
        c0 = src_cols[0]
        s = sc_ext[c0+1]
        dest_cr = col_ranges[c0+1]
        # clear
        for i in ru:
            for j in dest_cr:
                if out[i][j]!=0 and out[i][j]!=sc:
                    out[i][j]=0
        # copy
        for i in ru:
            for j in col_ranges[c0]:
                v = grid[i][j]
                if v!=0 and v!=sc:
                    dj = 2*s - j
                    out[i][dj] = v
    return out