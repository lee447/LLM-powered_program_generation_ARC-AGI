from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for v in row:
            counts[v] = counts.get(v, 0) + 1
    bg = max(counts, key=lambda k: counts[k])
    rowHas = [any(grid[i][j] != bg for j in range(C)) for i in range(R)]
    colHas = [any(grid[i][j] != bg for i in range(R)) for j in range(C)]
    minRow = next(i for i in range(R) if rowHas[i])
    maxRow = next(i for i in range(R-1, -1, -1) if rowHas[i])
    minCol = next(j for j in range(C) if colHas[j])
    maxCol = next(j for j in range(C-1, -1, -1) if colHas[j])
    rowSeps = [i for i in range(minRow, maxRow+1) if not rowHas[i]]
    colSeps = [j for j in range(minCol, maxCol+1) if not colHas[j]]
    res = [row[:] for row in grid]
    inner, outer = 2, 1
    for r in rowSeps:
        for j in range(C):
            res[r][j] = inner if minCol <= j <= maxCol else outer
    for c in colSeps:
        for i in range(R):
            res[i][c] = inner if minRow <= i <= maxRow else outer
    return res