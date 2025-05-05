from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    rings = []
    for s in (3, 4):
        for i in range(h - s + 1):
            for j in range(w - s + 1):
                c = grid[i][j]
                if c == 0:
                    continue
                ok = True
                for k in range(s):
                    if grid[i][j+k] != c or grid[i+s-1][j+k] != c:
                        ok = False
                    if grid[i+k][j] != c or grid[i+k][j+s-1] != c:
                        ok = False
                if not ok:
                    continue
                for di in range(1, s-1):
                    for dj in range(1, s-1):
                        if grid[i+di][j+dj] != 0:
                            ok = False
                if ok:
                    rings.append((c, s, i, j))
    out = [[0]*w for _ in range(h)]
    for c, s, i0, j0 in rings:
        if s == 3:
            ni = 0
        else:
            ni = h - s
        for di in range(s):
            for dj in range(s):
                if di in (0, s-1) or dj in (0, s-1):
                    out[ni+di][j0+dj] = c
    return out