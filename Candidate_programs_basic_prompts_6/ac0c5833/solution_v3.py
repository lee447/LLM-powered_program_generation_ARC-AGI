from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    rows = sorted({r for r in range(h) for c in range(w) if grid[r][c] == 4})
    cols = sorted({c for r in range(h) for c in range(w) if grid[r][c] == 4})
    row_bounds = [-1] + rows + [h]
    col_bounds = [-1] + cols + [w]
    cells = []
    for i in range(len(row_bounds) - 1):
        rs, re = row_bounds[i], row_bounds[i+1]
        if re - rs <= 1: continue
        for j in range(len(col_bounds) - 1):
            cs, ce = col_bounds[j], col_bounds[j+1]
            if ce - cs <= 1: continue
            cells.append((rs, cs, re, ce))
    shapes = []
    for rs, cs, re, ce in cells:
        pts = [(r - (rs + 1), c - (cs + 1)) for r in range(rs+1, re) for c in range(cs+1, ce) if grid[r][c] == 2]
        if pts:
            shapes.append(((rs, cs, re, ce), pts))
    if not shapes:
        return grid
    _, base_pts = max(shapes, key=lambda x: len(x[1]))
    base_set = set(base_pts)
    out = [row[:] for row in grid]
    for rs, cs, re, ce in cells:
        if not any(grid[r][c] == 2 for r in range(rs+1, re) for c in range(cs+1, ce)):
            for dr, dc in base_set:
                r, c = rs + 1 + dr, cs + 1 + dc
                if 0 <= r < h and 0 <= c < w and out[r][c] == 0:
                    out[r][c] = 2
    return out