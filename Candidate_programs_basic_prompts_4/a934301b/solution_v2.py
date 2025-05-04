from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [[0]*w for _ in range(h)]
    best = {}
    for r in range(h-1):
        for c in range(w-2):
            vals = [grid[r+i][c+j] for i in (0,1) for j in (0,1,2)]
            if 0 in vals: continue
            key = tuple(vals)
            pr, pc = best.get(key, (-1, -1))
            if c > pc or (c == pc and r > pr):
                best[key] = (r, c)
    for (r, c) in best.values():
        for i in (0,1):
            for j in (0,1,2):
                res[r+i][c+j] = grid[r+i][c+j]
    return res