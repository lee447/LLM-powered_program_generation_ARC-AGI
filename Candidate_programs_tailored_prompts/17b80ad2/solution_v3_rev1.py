from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [row[:] for row in grid]
    for j in range(w):
        anchors = [(i, grid[i][j]) for i in range(h) if grid[i][j] != 0]
        if not anchors:
            continue
        anchors.sort(key=lambda x: x[0])
        r0, c0 = anchors[0]
        for i in range(0, r0):
            out[i][j] = c0
        for (r_prev, _), (r_curr, c_curr) in zip(anchors, anchors[1:]):
            for i in range(r_prev + 1, r_curr):
                out[i][j] = c_curr
    return out