from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    r, c = len(grid), len(grid[0])
    b = grid[0][0]
    Y = [i for i in range(r) if all(grid[i][j] == b for j in range(c))]
    X = [j for j in range(c) if all(grid[i][j] == b for i in range(r))]
    if b > 4:
        xcut = X[1] + 1
        return [row[:xcut] for row in grid]
    if b > 1:
        ycut = Y[1] + 1
        return grid[:ycut]
    xcut = X[2] + 1
    ycut = Y[2] + 1
    return [row[:xcut] for row in grid[:ycut]]