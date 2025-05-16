from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = (n - 1) * 3 + 1
    out = [[0] * m for _ in range(m)]
    for i in range(1, n):
        for j in range(1, n):
            c = 9 if grid[i][j] != 7 else 7
            r0 = (i - 1) * 3 + 1
            c0 = (j - 1) * 3 + 1
            out[r0][c0] = c
            out[r0][c0 + 1] = c
            out[r0 + 1][c0] = c
            out[r0 + 1][c0 + 1] = c
    return out