from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0]) if H else 0
    out = [[0] * W for _ in range(H)]
    bounds = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                if v not in bounds:
                    bounds[v] = [r, r]
                else:
                    bounds[v][0] = min(bounds[v][0], r)
                    bounds[v][1] = max(bounds[v][1], r)
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                minr, maxr = bounds[v]
                out[minr + maxr - r][c] = v
    return out