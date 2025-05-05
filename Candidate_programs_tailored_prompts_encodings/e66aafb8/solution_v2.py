from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    r0, r1, c0, c1 = n, -1, n, -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    res = [[0]*w for _ in range(h)]
    if h > w:
        for i in range(h):
            sr = n - 1 - (r0 + i)
            for j in range(w):
                res[i][j] = grid[sr][c0 + j]
    else:
        for i in range(h):
            for j in range(w):
                sc = n - 1 - (c0 + j)
                res[i][j] = grid[r0 + i][sc]
    return res