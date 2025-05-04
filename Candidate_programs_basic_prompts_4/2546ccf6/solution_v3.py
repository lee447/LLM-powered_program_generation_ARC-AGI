from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    border_row = None
    c = None
    for i in range(H):
        v = grid[i][0]
        if v != 0 and all(grid[i][j] == v for j in range(W)):
            border_row = i
            c = v
            break
    border_col = None
    for j in range(W):
        if grid[0][j] == c and all(grid[i][j] == c for i in range(H)):
            border_col = j
            break
    if border_row is None or border_col is None:
        return grid
    h, w = border_row, border_col
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != 0:
                grid[i][border_col+1+j] = v
                grid[border_row+1+i][j] = v
                grid[border_row+1+i][border_col+1+j] = v
    return grid