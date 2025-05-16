from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = max(set(x for row in grid for x in row), key=lambda c: sum(r.count(c) for r in [grid]))
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != bg]
    cx, cy = (w - 1) / 2, (h - 1) / 2
    def rot90(r, c):
        dx, dy = c - cx, r - cy
        return int(round(cy - dx)), int(round(dx + cx))
    out = [[bg] * w for _ in range(h)]
    for r, c, v in pts:
        nr, nc = rot90(r, c)
        out[nr][nc] = v
    return out