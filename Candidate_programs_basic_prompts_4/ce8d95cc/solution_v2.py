from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    hb = {i for i,row in enumerate(grid) if len(set(row))==1}
    bars = []
    for j in range(n):
        col = [grid[i][j] for i in range(m) if i not in hb]
        if col and len(set(col))==1 and col[0]!=0:
            bars.append(j)
    bars.sort()
    bounds = [-1] + bars + [n]
    comp = []
    for i in range(m):
        row = grid[i]
        cr = []
        for a,b in zip(bounds, bounds[1:]):
            cr.append(row[a+1])
        comp.append(cr)
    res = []
    prev = None
    for r in comp:
        if r!=prev:
            res.append(r)
            prev = r
    return res