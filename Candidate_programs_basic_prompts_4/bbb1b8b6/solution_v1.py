from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    sep = next(j for j in range(w) if any(grid[i][j] == 5 for i in range(h)))
    L = [row[:sep] for row in grid]
    R = [row[sep+1:] for row in grid]
    m = len(L[0])
    count = 0
    for i in range(h):
        for j in range(m):
            if L[i][j] != 0 or R[i][j] != 0:
                count += 1
    if count == h * m:
        out = [[0]*m for _ in range(h)]
        for i in range(h):
            for j in range(m):
                if L[i][j] != 0:
                    out[i][j] = L[i][j]
                else:
                    out[i][j] = R[i][j]
        return out
    else:
        return L