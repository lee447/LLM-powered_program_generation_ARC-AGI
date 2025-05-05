from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    interior = range(1, h-1)
    zeros = {r: [c for c,v in enumerate(grid[r]) if v==0] for r in interior}
    for s in (1, -1):
        common = None
        for r in interior:
            ds = {c - s*r for c in zeros[r]}
            common = ds if common is None else common & ds
            if not common:
                break
        if common:
            d = next(iter(common))
            res = [row[:] for row in grid]
            for r in interior:
                c = s*r + d
                res[r][c] = 8
            return res
    return grid