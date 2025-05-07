import numpy as np

def solve(grid):
    arr = np.array(grid)
    reds = np.argwhere(arr==2)
    ys = np.argwhere(arr==4)
    rmin,cmin = reds.min(0)
    shape = set((r-rmin,c-cmin) for r,c in reds)
    ys_rows = sorted(set(y[0] for y in ys))
    ys_cols = sorted(set(y[1] for y in ys))
    dr = min(d for d in np.diff(ys_rows) if d>0)
    dc = min(d for d in np.diff(ys_cols) if d>0)
    out = arr.copy()
    for i in range(0,out.shape[0]//dr+1):
        for j in range(0,out.shape[1]//dc+1):
            base_r = ys_rows[0] + (i*dr) - rmin
            base_c = ys_cols[0] + (j*dc) - cmin
            for sr,sc in shape:
                rr,cc = base_r+sr, base_c+sc
                if 0<=rr<out.shape[0] and 0<=cc<out.shape[1] and out[rr,cc]==0:
                    out[rr,cc]=2
    return out.tolist()