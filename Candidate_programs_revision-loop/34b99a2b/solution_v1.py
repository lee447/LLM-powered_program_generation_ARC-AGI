from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    sep = next(j for j,v in enumerate(grid[0]) if v==4)
    width = min(sep, n - sep - 1)
    out = [[0]*width for _ in range(m)]
    for i in range(m):
        for j in range(width):
            l = grid[i][j]==8
            r = grid[i][sep+1+j]==5
            out[i][j] = 2 if l ^ r else 0
    return out