from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m = len(grid)
    if m == 0:
        return []
    n = len(grid[0])
    res = [row.copy() for row in grid]
    bottom = m - 1
    for j in range(n):
        if grid[bottom][j] != 0:
            pts = [(i, grid[i][j]) for i in range(m) if grid[i][j] != 0]
            prev = -1
            for i, v in pts:
                for ii in range(prev + 1, i + 1):
                    res[ii][j] = v
                prev = i
    return res