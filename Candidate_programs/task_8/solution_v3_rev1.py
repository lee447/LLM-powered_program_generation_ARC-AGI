from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    if H == 0:
        return grid
    W = len(grid[0])
    out = [row.copy() for row in grid]
    for c in range(W):
        if grid[H-1][c] != 5:
            continue
        pts = [(r, grid[r][c]) for r in range(H) if grid[r][c] != 0]
        if not pts:
            continue
        pts.sort()
        r0, v0 = pts[0]
        for r in range(r0 + 1):
            out[r][c] = v0
        for i in range(1, len(pts)):
            prev_r = pts[i-1][0]
            r_i, v_i = pts[i]
            for r in range(prev_r + 1, r_i + 1):
                out[r][c] = v_i
    return out