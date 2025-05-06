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
    block = [tuple(grid[r][c0:c1+1]) for r in range(r0, r1+1)]
    seen = []
    rows = []
    for row in block:
        if row not in seen:
            seen.append(row)
            rows.append(row)
    H = len(rows)
    W = c1 - c0 + 1
    out = [[0]*W for _ in range(H)]
    for i, row in enumerate(rows):
        nz = [j for j, x in enumerate(row) if x != 0]
        if nz:
            a, b = nz[0], nz[-1]
            out[i][a] = 8
            out[i][b] = 8
    return out