from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    tl = [[grid[h-1-i][w-1-j] for j in range(w)] for i in range(h)]
    H, W = 2*h, 2*w
    out = [[0]*W for _ in range(H)]
    for i in range(h):
        for j in range(w):
            v = tl[i][j]
            out[i][j] = v
            out[i][W-1-j] = v
            out[H-1-i][j] = v
            out[H-1-i][W-1-j] = v
    return out