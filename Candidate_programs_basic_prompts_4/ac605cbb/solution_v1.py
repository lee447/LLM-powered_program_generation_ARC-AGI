from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    pts.sort(key=lambda x: x[2])
    out = [row[:] for row in grid]
    for i in range(len(pts) - 1):
        r1, c1, col1 = pts[i]
        r2, c2, col2 = pts[i+1]
        if out[r1][c2] == 0:
            jr, jc = r1, c2
        else:
            jr, jc = r2, c1
        for c in range(min(c1, jc)+1, max(c1, jc)):
            out[r1][c] = 5
        for r in range(min(r1, jr)+1, max(r1, jr)):
            out[r][c1] = 5
        for r in range(min(jr, r2)+1, max(jr, r2)):
            out[r][jc] = 5
        for c in range(min(jc, c2)+1, max(jc, c2)):
            out[r2][c] = 5
        out[jr][jc] = 4
        out[r1][c1] = col1
        out[r2][c2] = col2
    return out