from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    row = grid[0]
    N = len(row)
    pos = row.index(2)
    out = [[0]*N for _ in range(N)]
    for r in range(N):
        x1 = pos - r
        x2 = pos + r
        if 0 <= x1 < N: out[r][x1] = 2
        if 0 <= x2 < N: out[r][x2] = 2
    for r in range(N):
        k = (N-1) - r
        x1 = pos - k
        x2 = pos + k
        if 0 <= x1 < N and out[r][x1] == 0: out[r][x1] = 1
        if 0 <= x2 < N and out[r][x2] == 0: out[r][x2] = 1
    return out