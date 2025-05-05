from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0])
    for d in range(W):
        if all(grid[r][d] == 4 for r in range(H)):
            break
    res = [[0] * d for _ in range(H)]
    for r in range(H):
        L = [False] * d
        R = [False] * d
        for c in range(d):
            if grid[r][c] == 8:
                L[c] = True
        for c in range(d+1, W):
            if grid[r][c] == 5:
                m = d - 1 - (c - (d + 1))
                if 0 <= m < d:
                    R[m] = True
        for c in range(d):
            if L[c] ^ R[c]:
                res[r][c] = 2
    return res