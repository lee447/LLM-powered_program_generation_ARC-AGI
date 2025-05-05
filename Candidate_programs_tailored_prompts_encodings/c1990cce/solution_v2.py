from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    N = len(grid[0])
    c = grid[0].index(2)
    out = [[0]*N for _ in range(N)]
    for i in range(N):
        j1 = c + i
        if 0 <= j1 < N:
            out[i][j1] = 2
        j2 = c - i
        if 0 <= j2 < N:
            out[i][j2] = 2
    k = 1
    while True:
        d = c - 4*k
        if d < -(N-1):
            break
        for i in range(N):
            j = i + d
            if 0 <= j < N and j >= c - i and j <= c + i and out[i][j] == 0:
                out[i][j] = 1
        k += 1
    return out