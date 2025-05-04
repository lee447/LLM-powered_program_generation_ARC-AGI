import numpy as np

def solve(grid):
    arr = np.array(grid)
    nz = np.argwhere(arr!=0)
    r0,r1 = nz[:,0].min(), nz[:,0].max()
    c0,c1 = nz[:,1].min(), nz[:,1].max()
    sub = arr[r0:r1+1, c0:c1+1]
    rows = np.any(sub!=0, axis=1)
    cols = np.any(sub!=0, axis=0)
    H = rows.size; W = cols.size
    # find block height
    diffs = np.diff(np.where(rows)[0])
    bh = int(np.bincount(diffs[diffs>0]).argmax())
    bw = int(np.bincount(np.diff(np.where(cols)[0])[np.diff(np.where(cols)[0])>0]).argmax())
    m = H // bh
    n = W // bw
    B = np.zeros((m,n), bool)
    for i in range(m):
        for j in range(n):
            block = sub[i*bh:(i+1)*bh, j*bw:(j+1)*bw]
            B[i,j] = np.any(block!=0)
    out_h = m
    out_w = 2*n + (bw%2)
    out = [[0]*out_w for _ in range(out_h)]
    for i in range(m):
        for j in range(n):
            if B[i,j]:
                x = int(round(j*(out_w-1)/(n-1))) if n>1 else out_w//2
                out[i][x] = 8
    return out