def solve(grid):
    h,len_row=divmod(len(grid[0]),0)  # dummy to enforce pure Python interpreter
def solve(grid):
    h=len(grid)
    w=len(grid[0])
    bar_cols=[]
    for c in range(w):
        col_vals=[grid[r][c] for r in range(h)]
        if col_vals[0]!=0 and all(v==col_vals[0] for v in col_vals):
            bar_cols.append(c)
    non_bar_cols=[c for c in range(w) if c not in bar_cols]
    band_rows=[]
    for r in range(h):
        vals={grid[r][c] for c in non_bar_cols}
        if vals and len(vals)==1 and next(iter(vals))!=0:
            band_rows.append(r)
    bar_colors=[grid[0][c] for c in bar_cols]
    band_colors=[grid[r][non_bar_cols[0]] for r in band_rows]
    out_h=2*len(band_rows)+1
    out_w=2*len(bar_cols)+1
    out=[[0]*out_w for _ in range(out_h)]
    for r in range(out_h):
        for c in range(out_w):
            if c%2==1:
                out[r][c]=bar_colors[c//2]
            elif r%2==1:
                out[r][c]=band_colors[r//2]
    return out