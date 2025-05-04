from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    positions5 = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == 5]
    axis_row = max(i for i, j in positions5)
    axis_col = max(j for i, j in positions5)
    target = None
    for i in range(axis_row):
        for j in range(axis_col):
            if grid[i][j] not in (0, 5):
                target = grid[i][j]
                break
        if target is not None:
            break
    out = [[grid[i][j] for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] == target and not (i < axis_row and j < axis_col):
                out[i][j] = 0
    return out