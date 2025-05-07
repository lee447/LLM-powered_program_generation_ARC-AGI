from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    min_r, max_r = h, -1
    min_c, max_c = w, -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                if i < min_r: min_r = i
                if i > max_r: max_r = i
                if j < min_c: min_c = j
                if j > max_c: max_c = j
    empty_rows = []
    for r in range(min_r, max_r + 1):
        if all(grid[r][c] == 0 for c in range(min_c, max_c + 1)):
            empty_rows.append(r)
    if empty_rows:
        for r in empty_rows:
            for c in range(w):
                grid[r][c] = 3
    else:
        empty_cols = []
        for c in range(min_c, max_c + 1):
            if all(grid[r][c] == 0 for r in range(min_r, max_r + 1)):
                empty_cols.append(c)
        for c in empty_cols:
            for r in range(h):
                grid[r][c] = 3
    return grid