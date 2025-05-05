import numpy as np

def solve(grid):
    h,w = len(grid), len(grid[0])
    arr = np.array(grid)
    rcnt = np.count_nonzero(arr==5, axis=1)
    sep_rows = []
    for i in range(h):
        if rcnt[i] >= 2:
            sep_rows.append(i)
    if not sep_rows:
        return grid
    r0, r1 = min(sep_rows), max(sep_rows)
    ccnt = np.count_nonzero(arr[r0:r1+1]==5, axis=0)
    sep_cols = []
    for j in range(w):
        if ccnt[j] >= 2:
            sep_cols.append(j)
    col_segs = []
    start = None
    for j in range(w):
        if j not in sep_cols:
            if start is None:
                start = j
        else:
            if start is not None:
                col_segs.append((start, j-1))
                start = None
    if start is not None:
        col_segs.append((start, w-1))
    row_segs = [(0, r0-1)] if r0>0 else []
    if r1 < h-1:
        row_segs.append((r1+1, h-1))
    blocks = []
    for rs, re in row_segs:
        for cs, ce in col_segs:
            Q = [row[cs:ce+1] for row in grid[rs:re+1]]
            H, W = len(Q), len(Q[0])
            for th in range(1, H+1):
                if H % th: continue
                for tw in range(1, W+1):
                    if W % tw: continue
                    ok = True
                    for i in range(H):
                        for j in range(W):
                            if Q[i][j] != Q[i%th][j%tw]:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        T = [row[:tw] for row in Q[:th]]
                        blocks.append(T)
                        th = H+1
                        break
                else:
                    continue
                break
    best = None
    best_area = None
    for T in blocks:
        s = set(sum(T,[])) - {7,5}
        if len(s)==2:
            area = len(T)*len(T[0])
            if best is None or area < best_area:
                best, best_area = T, area
    return best if best is not None else grid