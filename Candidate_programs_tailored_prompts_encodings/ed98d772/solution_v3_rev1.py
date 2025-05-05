from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    rot0 = grid
    rot90ccw = [[grid[j][n-1-i] for j in range(n)] for i in range(n)]
    rot180 = [row[::-1] for row in grid[::-1]]
    rot90cw = [[grid[n-1-j][i] for j in range(n)] for i in range(n)]
    out = []
    for i in range(n):
        out.append(rot0[i] + rot90ccw[i])
    for i in range(n):
        out.append(rot180[i] + rot90cw[i])
    return out