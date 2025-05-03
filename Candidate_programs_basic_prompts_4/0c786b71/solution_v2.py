from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    H = 2 * h
    W = 2 * w
    res = [[0] * W for _ in range(H)]
    for i in range(H):
        mi = i if i < h else H - 1 - i
        for j in range(W):
            mj = j if j < w else W - 1 - j
            res[i][j] = grid[h - 1 - mi][w - 1 - mj]
    return res