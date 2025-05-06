from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    pts = [(r, c) for r in range(n) for c in range(m) if grid[r][c] != 0]
    if not pts:
        return []
    r0 = min(r for r, c in pts)
    r1 = max(r for r, c in pts)
    c0 = min(c for r, c in pts)
    c1 = max(c for r, c in pts)
    block = [grid[r][c0:c1+1] for r in range(r0, r1+1)]
    compressed_rows = []
    prev = None
    for row in block:
        if row != prev:
            compressed_rows.append(row)
            prev = row
    cols = list(zip(*compressed_rows))
    compressed_cols = []
    prev = None
    for col in cols:
        if col != prev:
            compressed_cols.append(col)
            prev = col
    kernel = [list(row) for row in zip(*compressed_cols)]
    H, W = len(kernel), len(kernel[0]) if kernel else (0, 0)
    out = [[8 if kernel[i][j] != 0 else 0 for j in range(W)] for i in range(H)]
    return out