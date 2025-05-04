import numpy as np

def solve(grid):
    pairs = [c for c in range(len(grid[0])) if grid[0][c] == 2 and grid[1][c] == 2]
    n = len(pairs)
    h = 2*n - 2
    w = n + 2
    out = [[0]*w for _ in range(h)]
    center = w//2
    out[0][center] = 3
    diffs = np.diff(pairs)
    row = 1
    col = center
    if diffs[0] < 3:
        col -= 1
    for i,d in enumerate(diffs):
        if i % 2 == 0:
            for dc in (0,1):
                out[row][col+dc] = 2
            row += 1
        else:
            shift = 1 if d >= 3 else 0
            for dr in (0,1):
                out[row+dr][col+shift] = 2
            col += shift
            row += 2
    return out