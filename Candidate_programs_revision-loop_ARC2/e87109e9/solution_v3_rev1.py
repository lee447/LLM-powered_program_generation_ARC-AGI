import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    top_bg = grid[0][0]
    bottom_start = 0
    for i in range(h):
        if all(grid[i][j] != 0 for j in range(w)) and any(grid[i][j] != top_bg for j in range(w)):
            bottom_start = i
            break
    bottom = [row[:] for row in grid[bottom_start:]]
    H = len(bottom)
    W = w
    coords = [(r, c) for r in range(H) for c in range(W) if bottom[r][c] == 8]
    new = [row[:] for row in bottom]
    for r, c in coords:
        for rr in (r, H-1-r):
            for cc in (c, W-1-c):
                new[rr][cc] = 8
    return new