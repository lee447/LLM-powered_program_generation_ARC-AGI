from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    nrows, ncols = len(grid), len(grid[0])
    last = nrows - 1
    W = 0
    for j in range(ncols - 1, -1, -1):
        if grid[last][j] == 8:
            W += 1
        else:
            break
    H = 0
    for i in range(nrows - 1, -1, -1):
        if all(grid[i][j] == 8 for j in range(ncols - W, ncols)):
            H += 1
        else:
            break
    c1, c2 = ncols - 2*W, ncols - W
    r1 = nrows - H
    return [row[c1:c2] for row in grid[r1:]]