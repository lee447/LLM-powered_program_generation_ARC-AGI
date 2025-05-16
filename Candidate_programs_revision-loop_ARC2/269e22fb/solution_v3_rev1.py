from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    H = W = 20
    rem_h = H - h
    rem_w = W - w
    half_h = rem_h // 2
    half_w = rem_w // 2
    out = [[0] * W for _ in range(H)]
    for i in range(H):
        if i < h:
            ri = i
        elif i < h + half_h:
            ri = h - 1 - (i - h)
        else:
            ri = i - (h + half_h)
        for j in range(W):
            if j < w:
                cj = j
            elif j < w + half_w:
                cj = w - 1 - (j - w)
            else:
                cj = j - (w + half_w)
            out[i][j] = grid[ri][cj]
    return out