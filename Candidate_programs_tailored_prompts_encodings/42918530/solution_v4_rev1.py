from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_rows = {i for i in range(H) if all(c==0 for c in grid[i])}
    zero_cols = {j for j in range(W) if all(grid[i][j]==0 for i in range(H))}
    row_segs = []
    start = None
    for i in range(H):
        if i not in zero_rows:
            if start is None: start = i
        else:
            if start is not None:
                row_segs.append((start, i-1))
                start = None
    if start is not None:
        row_segs.append((start, H-1))
    col_segs = []
    start = None
    for j in range(W):
        if j not in zero_cols:
            if start is None: start = j
        else:
            if start is not None:
                col_segs.append((start, j-1))
                start = None
    if start is not None:
        col_segs.append((start, W-1))
    out = [row[:] for row in grid]
    refs = {}
    masks = {}
    for r0,r1 in row_segs:
        for c0,c1 in col_segs:
            color = grid[r0][c0]
            h = r1 - r0 + 1
            w = c1 - c0 + 1
            ih, iw = h-2, w-2
            mask = [[False]*iw for _ in range(ih)]
            has = False
            for i in range(ih):
                for j in range(iw):
                    if grid[r0+1+i][c0+1+j] != 0:
                        mask[i][j] = True
                        has = True
            if has:
                refs[color] = mask
    for r0,r1 in row_segs:
        for c0,c1 in col_segs:
            color = grid[r0][c0]
            if color not in refs: continue
            mask = refs[color]
            h = r1-r0+1
            w = c1-c0+1
            ih, iw = h-2, w-2
            for i in range(ih):
                for j in range(iw):
                    if mask[i][j]:
                        out[r0+1+i][c0+1+j] = color
    return out