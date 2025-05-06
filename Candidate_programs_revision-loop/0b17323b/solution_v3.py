from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h > 0 else 0
    new = [row.copy() for row in grid]
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    if len(pts) >= 2:
        pts.sort()
        dr = pts[1][0] - pts[0][0]
        dc = pts[1][1] - pts[0][1]
        r, c = pts[-1]
        while 0 <= r + dr < h and 0 <= c + dc < w:
            r += dr
            c += dc
            new[r][c] = 2
    return new