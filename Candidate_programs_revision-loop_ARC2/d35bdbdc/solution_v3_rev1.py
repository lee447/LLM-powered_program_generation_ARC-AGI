import numpy as np
from collections import Counter
def solve(grid):
    h, w = len(grid), len(grid[0])
    rings = []
    for i in range(h-2):
        for j in range(w-2):
            b = grid[i][j]
            if b == 0: continue
            ok = True
            for x in range(3):
                for y in range(3):
                    if x in (0,2) or y in (0,2):
                        if grid[i+x][j+y] != b: ok = False
                    else:
                        if grid[i+x][j+y] == b: ok = False
            if ok:
                rings.append((i, j, b, grid[i+1][j+1]))
    if not rings:
        return [row[:] for row in grid]
    cnt = Counter(c for row in grid for c in row if c)
    cluster = max(cnt, key=lambda c: cnt[c])
    removed = []
    kept = []
    for r in rings:
        i,j,b,bc = r
        rem_flag = False
        for x in range(3):
            for y in range(3):
                if grid[i+x][j+y] == cluster:
                    rem_flag = True
        if rem_flag:
            removed.append(r)
        else:
            kept.append(r)
    if not kept:
        kept = rings
        removed = []
    if removed:
        sel = min(removed, key=lambda r: (abs(r[2]-cluster), r[2]))
        sel_bc = sel[3]
    else:
        sel_bc = kept[0][3]
    kept_sorted = sorted(kept, key=lambda r: r[2])
    new_bcs = []
    if len(kept_sorted) == 1:
        new_bcs = [sel_bc]
    elif len(kept_sorted) == 2:
        new_bcs = [sel_bc, kept_sorted[0][2]]
    else:
        for idx,r in enumerate(kept_sorted):
            if idx==0:
                new_bcs.append(sel_bc)
            elif idx==1:
                new_bcs.append(kept_sorted[0][2])
            else:
                new_bcs.append(r[3])
    out = [row[:] for row in grid]
    for i,j,b,bc in rings:
        for x in range(3):
            for y in range(3):
                out[i+x][j+y] = 0
    for (i,j,b,bc),nc in zip(kept_sorted,new_bcs):
        for x in range(3):
            for y in range(3):
                if x in (0,2) or y in (0,2):
                    out[i+x][j+y] = b
        out[i+1][j+1] = nc
    return out