from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    r90cw = [[grid[n-1-j][i] for j in range(n)] for i in range(n)]
    r90ccw = [[grid[j][n-1-i] for j in range(n)] for i in range(n)]
    r180 = [row[::-1] for row in grid[::-1]]
    out = []
    for i in range(n):
        out.append(grid[i] + r90ccw[i])
    for i in range(n):
        out.append(r180[i] + r90cw[i])
    return out