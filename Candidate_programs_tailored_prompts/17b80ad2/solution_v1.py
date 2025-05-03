from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0])
    out = [row[:] for row in grid]
    anchors = set(c for r in range(H) for c in range(W) if grid[r][c] == 5)
    for c in sorted(anchors):
        color_rows = {}
        for r in range(H):
            v = grid[r][c]
            if v != 0:
                if v not in color_rows or r > color_rows[v]:
                    color_rows[v] = r
        if not color_rows:
            continue
        bc = sorted((r, v) for v, r in color_rows.items())
        prev = 0
        for r, v in bc:
            for rr in range(prev, r + 1):
                out[rr][c] = v
            prev = r + 1
    return out