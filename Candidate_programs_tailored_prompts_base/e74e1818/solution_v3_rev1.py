from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    res = [row[:] for row in grid]
    colors = {val for row in grid for val in row if val != 0}
    for color in colors:
        coords = [(i, j) for i in range(h) for j in range(w) if orig[i][j] == color]
        minr = min(i for i, j in coords)
        maxr = max(i for i, j in coords)
        minc = min(j for i, j in coords)
        maxc = max(j for i, j in coords)
        sub = [orig[i][minc:maxc+1] for i in range(minr, maxr+1)]
        rev = sub[::-1]
        for di, row in enumerate(rev):
            for dj, val in enumerate(row):
                res[minr+di][minc+dj] = val
    return res