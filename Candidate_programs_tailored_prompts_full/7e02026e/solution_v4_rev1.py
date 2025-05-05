import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    fills = []
    for i in range(1, h-1):
        for j in range(1, w-1):
            if grid[i][j] == 3:
                up, down, left, right = grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]
                neigh = [up, down, left, right]
                if any(n == 3 for n in neigh) and any(n == 0 for n in neigh) and all(n in (0, 3) for n in neigh):
                    if up == 0: fills.append((i-1, j))
                    if down == 0: fills.append((i+1, j))
                    if left == 0: fills.append((i, j-1))
                    if right == 0: fills.append((i, j+1))
    for i, j in fills:
        grid[i][j] = 3
    return grid