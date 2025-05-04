from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    empty_rows = [i for i in range(h) if all(grid[i][j] == 0 for j in range(w))]
    empty_cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    split_row = None
    for i in empty_rows:
        above = any(grid[r][c] != 0 for r in range(i) for c in range(w))
        below = any(grid[r][c] != 0 for r in range(i+1, h) for c in range(w))
        if above and below:
            split_row = i
            break
    split_col = None
    if split_row is None:
        for j in empty_cols:
            left = any(grid[r][c] != 0 for r in range(h) for c in range(j))
            right = any(grid[r][c] != 0 for r in range(h) for c in range(j+1, w))
            if left and right:
                split_col = j
                break
    res = [row[:] for row in grid]
    if split_row is not None:
        for j in range(w):
            res[split_row][j] = 3
    elif split_col is not None:
        for i in range(h):
            res[i][split_col] = 3
    return res