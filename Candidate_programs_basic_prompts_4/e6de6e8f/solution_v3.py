from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    top = [j for j,v in enumerate(grid[0]) if v==2]
    bottom = [j for j,v in enumerate(grid[1]) if v==2]
    H = len(bottom)
    W = H-1
    out = [[0]*W for _ in range(H)]
    mid = W//2
    out[0][mid] = 3
    tbin = [bottom.index(x) for x in top]
    cur_row, cur_col = 0, mid
    for k in range(1, len(tbin)):
        tgt = tbin[k] - 1
        if tgt < cur_row:
            tgt = cur_row
        for r in range(cur_row+1, min(tgt+1, H)):
            out[r][cur_col] = 2
        cur_row = min(tgt, H-1)
        if k < len(tbin)-1 and cur_col+1 < W:
            out[cur_row][cur_col+1] = 2
            cur_col += 1
    for r in range(cur_row+1, H):
        out[r][cur_col] = 2
    return out