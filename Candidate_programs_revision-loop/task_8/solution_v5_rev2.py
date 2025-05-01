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
    propag = {c: pts for c, pts in cols.items() if any(r == h-1 for r, _ in pts)}
    for r in range(h):
        for c in range(w):
            if c not in propag:
                out[r][c] = grid[r][c]
            else:
                if grid[r][c]:
                    out[r][c] = grid[r][c]
                else:
                    pts = sorted(propag[c])
                    val = 0
                    for nr, nv in pts:
                        if nr > r:
                            val = nv
                            break
                    out[r][c] = val
    return out