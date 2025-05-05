from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    vals = set()
    for row in grid:
        for v in row:
            vals.add(v)
    k = len(vals)
    h = len(grid)
    w = len(grid[0])
    out = []
    for mi in range(k):
        for i in range(h):
            row = []
            for mj in range(k):
                for j in range(w):
                    row.append(grid[i][j])
            out.append(row)
    return out