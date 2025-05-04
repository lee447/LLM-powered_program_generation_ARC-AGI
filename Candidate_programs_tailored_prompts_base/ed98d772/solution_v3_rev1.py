from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    rot90 = [[grid[n-1-j][i] for j in range(n)] for i in range(n)]
    rot180 = [[grid[n-1-i][n-1-j] for j in range(n)] for i in range(n)]
    rot270 = [[grid[j][n-1-i] for j in range(n)] for i in range(n)]
    rotations = [grid, rot90, rot180, rot270]
    out = [[0] * (2*n) for _ in range(2*n)]
    for p in range(2):
        for q in range(2):
            k = (2*p + 3*q) % 4
            block = rotations[k]
            for i in range(n):
                for j in range(n):
                    out[p*n + i][q*n + j] = block[i][j]
    return out