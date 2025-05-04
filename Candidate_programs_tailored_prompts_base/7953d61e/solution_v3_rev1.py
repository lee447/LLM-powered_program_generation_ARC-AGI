from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    rotccw = [[grid[c][n-1-r] for c in range(n)] for r in range(n)]
    rothr = [[grid[n-1-r][n-1-c] for c in range(n)] for r in range(n)]
    rotcw = [[grid[n-1-c][r] for c in range(n)] for r in range(n)]
    res = []
    for r in range(n):
        res.append(grid[r] + rotccw[r])
    for r in range(n):
        res.append(rothr[r] + rotcw[r])
    return res