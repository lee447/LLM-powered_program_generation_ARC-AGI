from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    rows = [i for i in range(R) for j in range(C) if grid[i][j] == 8]
    cols = [j for i in range(R) for j in range(C) if grid[i][j] == 8]
    rmin, rmax = min(rows), max(rows)
    cmin, cmax = min(cols), max(cols)
    h = rmax - rmin + 1
    w = cmax - cmin + 1
    bad = {0, 2, 5, 8}
    for i in range(R - h + 1):
        for j in range(C - w + 1):
            ok = True
            for di in range(h):
                for dj in range(w):
                    v = grid[i + di][j + dj]
                    if v in bad:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return [grid[i + di][j : j + w] for di in range(h)]
    return []