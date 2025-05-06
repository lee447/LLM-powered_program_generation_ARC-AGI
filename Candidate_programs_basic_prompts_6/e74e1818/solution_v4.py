from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    res = [[0]*w for _ in range(h)]
    colors = {grid[i][j] for i in range(h) for j in range(w) if grid[i][j]!=0}
    for c in colors:
        rmin, rmax, cmin, cmax = h, -1, w, -1
        for i in range(h):
            for j in range(w):
                if grid[i][j]==c:
                    if i<rmin: rmin=i
                    if i>rmax: rmax=i
                    if j<cmin: cmin=j
                    if j>cmax: cmax=j
        if rmax<rmin or cmax<cmin: continue
        for i in range(rmax-rmin+1):
            for j in range(cmax-cmin+1):
                res[rmin+i][cmin+j] = grid[rmax-i][cmin+j]
    return res