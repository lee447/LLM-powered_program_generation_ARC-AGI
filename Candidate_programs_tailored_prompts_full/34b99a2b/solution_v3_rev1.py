from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0])
    for d in range(W):
        if all(grid[r][d] == 4 for r in range(H)):
            break
    k = min(d, W - d - 1)
    res = [[0] * k for _ in range(H)]
    for r in range(H):
        for c in range(k):
            if (grid[r][c] == 8) ^ (grid[r][d + 1 + c] == 5):
                res[r][c] = 2
    return res