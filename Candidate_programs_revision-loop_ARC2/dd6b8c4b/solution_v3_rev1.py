from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2:
                cr, cc = i, j
    up = all(0 <= cr-1 < h and 0 <= cc+dc < w and grid[cr-1][cc+dc] == 6 for dc in (-1, 0, 1))
    down = all(0 <= cr+1 < h and 0 <= cc+dc < w and grid[cr+1][cc+dc] == 6 for dc in (-1, 0, 1))
    left = all(0 <= cr+dr < h and 0 <= cc-1 < w and grid[cr+dr][cc-1] == 6 for dr in (-1, 0, 1))
    right = all(0 <= cr+dr < h and 0 <= cc+1 < w and grid[cr+dr][cc+1] == 6 for dr in (-1, 0, 1))
    if up and down and left and right:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                r, c = cr+dr, cc+dc
                if (dr, dc) != (0, 0) and 0 <= r < h and 0 <= c < w and grid[r][c] == 3:
                    g[r][c] = 9
    else:
        if up:
            for dc in (-1, 0, 1):
                r, c = cr-1, cc+dc
                if 0 <= r < h and 0 <= c < w and grid[r][c] == 3:
                    g[r][c] = 9
        if down:
            for dc in (-1, 0, 1):
                r, c = cr+1, cc+dc
                if 0 <= r < h and 0 <= c < w and grid[r][c] == 3:
                    g[r][c] = 9
        if left:
            for dr in (-1, 0, 1):
                r, c = cr+dr, cc-1
                if 0 <= r < h and 0 <= c < w and grid[r][c] == 3:
                    g[r][c] = 9
        if right:
            for dr in (-1, 0, 1):
                r, c = cr+dr, cc+1
                if 0 <= r < h and 0 <= c < w and grid[r][c] == 3:
                    g[r][c] = 9
    return g