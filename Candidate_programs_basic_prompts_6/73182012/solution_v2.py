from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rmin, rmax = len(grid), -1
    cmin, cmax = len(grid[0]), -1
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v != 0:
                if i < rmin: rmin = i
                if i > rmax: rmax = i
                if j < cmin: cmin = j
                if j > cmax: cmax = j
    h = rmax - rmin + 1
    w = cmax - cmin + 1
    hh, ww = h // 2, w // 2
    return [row[cmin:cmin+ww] for row in grid[rmin:rmin+hh]]