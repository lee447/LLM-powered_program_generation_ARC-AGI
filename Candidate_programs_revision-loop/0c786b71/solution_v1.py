from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    seed = [row[::-1] for row in grid[::-1]]
    seed_lr = [row[::-1] for row in seed]
    seed_v = seed[::-1]
    seed_v_lr = [row[::-1] for row in seed_v]
    out = [[0] * (2 * n) for _ in range(2 * m)]
    for i in range(2 * m):
        for j in range(2 * n):
            if i < m and j < n:
                out[i][j] = seed[i][j]
            elif i < m:
                out[i][j] = seed_lr[i][j - n]
            elif j < n:
                out[i][j] = seed_v[i - m][j]
            else:
                out[i][j] = seed_v_lr[i - m][j - n]
    return out