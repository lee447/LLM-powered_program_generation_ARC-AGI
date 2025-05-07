from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    color = next(cell for row in grid for cell in row if cell != 0)
    pblock = [[color if grid[r][c] == 0 else 0 for c in range(n)] for r in range(n)]
    out = [[0] * (n * n) for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                for r in range(n):
                    for c in range(n):
                        out[i*n + r][j*n + c] = pblock[r][c]
    return out