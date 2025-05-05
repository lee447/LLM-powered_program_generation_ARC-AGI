from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    colors = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                if v not in colors:
                    colors[v] = [r, r, c, c]
                else:
                    colors[v][0] = min(colors[v][0], r)
                    colors[v][1] = max(colors[v][1], r)
                    colors[v][2] = min(colors[v][2], c)
                    colors[v][3] = max(colors[v][3], c)
    best = None
    for v, (r0, r1, c0, c1) in colors.items():
        area = (r1 - r0 + 1) * (c1 - c0 + 1)
        key = (area, -r0, -c0, v)
        if best is None or key > best[0]:
            best = (key, v, r0, r1, c0, c1)
    _, v, r0, r1, c0, c1 = best
    out = [[0] * (c1 - c0 + 1) for _ in range(r1 - r0 + 1)]
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            if grid[r][c] == v:
                out[r - r0][c - c0] = v
    return out