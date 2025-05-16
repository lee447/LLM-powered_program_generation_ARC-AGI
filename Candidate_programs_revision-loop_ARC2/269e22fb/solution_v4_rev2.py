from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    H = W = 20
    out = [[0]*W for _ in range(H)]
    for i in range(H):
        bi = (i // h) & 1
        ti = i % h
        ri = h - 1 - ti if bi else ti
        for j in range(W):
            bj = (j // w) & 1
            tj = j % w
            cj = w - 1 - tj if bj else tj
            out[i][j] = grid[ri][cj]
    return out