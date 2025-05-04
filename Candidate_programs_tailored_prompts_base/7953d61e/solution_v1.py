from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    cols = [[grid[i][j] for i in range(n)] for j in range(n)]
    out = []
    for k in range(n):
        out.append(grid[k] + cols[n-1-k])
    for k in range(n):
        out.append(grid[n-1-k][::-1] + cols[k][::-1])
    return out