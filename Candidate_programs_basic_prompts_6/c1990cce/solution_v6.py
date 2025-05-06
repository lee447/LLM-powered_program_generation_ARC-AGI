from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    row = grid[0]
    N = len(row)
    c = row.index(2)
    out = [[0]*N for _ in range(N)]
    for i in range(N):
        j1 = c - i
        j2 = c + i
        if 0 <= j1 < N and i <= c:
            out[i][j1] = 2
        if 0 <= j2 < N and i <= c:
            out[i][j2] = 2
    for start_j, dj in ((0,1),(2*c,-1)):
        i, j = c, start_j
        while True:
            i += 1
            j += dj
            if not (0 <= i < N and 0 <= j < N):
                break
            if out[i][j] == 0:
                out[i][j] = 1
    return out