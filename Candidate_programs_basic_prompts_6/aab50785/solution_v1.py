from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = []
    for i in range(h - 1):
        js = []
        for j in range(w - 1):
            if grid[i][j] == 8 and grid[i][j+1] == 8 and grid[i+1][j] == 8 and grid[i+1][j+1] == 8:
                js.append(j)
        if len(js) >= 2:
            j1, j2 = js[0], js[1]
            s, e = j1 + 2, j2 - 1
            res.append(grid[i][s:e+1])
            res.append(grid[i+1][s:e+1])
    return res