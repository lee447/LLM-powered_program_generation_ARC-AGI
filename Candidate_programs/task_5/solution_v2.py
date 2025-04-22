from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    A = [row[::-1] for row in grid[::-1]]
    res = []
    for i in range(2*h):
        i_m = i if i < h else 2*h - 1 - i
        row = []
        for j in range(2*w):
            j_m = j if j < w else 2*w - 1 - j
            row.append(A[i_m][j_m])
        res.append(row)
    return res