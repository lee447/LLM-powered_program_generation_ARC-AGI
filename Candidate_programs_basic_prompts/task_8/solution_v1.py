from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    out = [[0]*w for _ in range(h)]
    for c in range(w):
        if grid[h-1][c] != 0:
            d = {}
            for r in range(h):
                v = grid[r][c]
                if v:
                    d.setdefault(v, []).append(r)
            groups = sorted(d.items(), key=lambda kv: min(kv[1]))
            prev = -1
            for v, rs in groups:
                m = max(rs)
                if m > prev:
                    for r in range(prev+1, m+1):
                        out[r][c] = v
                    prev = m
        else:
            for r in range(h):
                out[r][c] = grid[r][c]
    return out