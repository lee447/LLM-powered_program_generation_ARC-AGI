from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    cols = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                cols.setdefault(c, []).append((r, v))
    for c, pts in cols.items():
        if len(pts) == 1:
            r, v = pts[0]
            out[r][c] = v
        else:
            pts.sort()
            rows, vals = zip(*pts)
            for r in range(h):
                if grid[r][c]:
                    out[r][c] = grid[r][c]
                else:
                    for nr, nv in pts:
                        if nr > r:
                            out[r][c] = nv
                            break
                    else:
                        out[r][c] = pts[-1][1]
    return out