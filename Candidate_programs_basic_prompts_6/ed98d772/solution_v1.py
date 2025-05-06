from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    out = []
    for i in range(n):
        left = grid[i]
        right = [grid[j][n-1-i] for j in range(n)]
        out.append(left+right)
    for i in range(n):
        left = [grid[n-1-i][n-1-j] for j in range(n)]
        right = [grid[n-1-j][i] for j in range(n)]
        out.append(left+right)
    return out