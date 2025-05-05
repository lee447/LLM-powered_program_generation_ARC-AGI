from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    colors = set(v for row in grid for v in row if v != 0)
    f = len(colors)
    out = []
    for i in range(h * f):
        gi = i % h
        row = []
        for j in range(w * f):
            row.append(grid[gi][j % w])
        out.append(row)
    return out