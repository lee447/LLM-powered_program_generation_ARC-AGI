from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    row0 = grid[0]
    n = len(row0)
    c = row0.index(2)
    out = [[0]*n for _ in range(n)]
    R = min(c, n-1-c)
    for i in range(R+1):
        j1 = c - i
        j2 = c + i
        if 0 <= j1 < n:
            out[i][j1] = 2
        if 0 <= j2 < n:
            out[i][j2] = 2
    for i in range(2, R+1, 2):
        x, y = i, c - i
        d = 1
        while x + d < n and y + d < n:
            if out[x+d][y+d] == 0:
                out[x+d][y+d] = 1
            d += 1
    return out