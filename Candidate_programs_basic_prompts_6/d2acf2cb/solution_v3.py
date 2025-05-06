from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    res = [row[:] for row in grid]
    mapping = {0:8, 8:0, 6:7, 7:6}
    marker_rows = [r for r in range(h) if sum(1 for c in range(w) if grid[r][c]==4) >= 2]
    if len(marker_rows) == 2:
        r1, r2 = sorted(marker_rows)
        cols = [c for c in range(w) if grid[r1][c] == 4]
        if len(cols) >= 2:
            c1, c2 = min(cols), max(cols)
            for r in range(r1+1, r2):
                for c in (c1, c2):
                    v = res[r][c]
                    if v in mapping:
                        res[r][c] = mapping[v]
    else:
        for r in marker_rows:
            cols = [c for c in range(w) if grid[r][c] == 4]
            if cols:
                c1, c2 = min(cols), max(cols)
                for c in range(c1+1, c2):
                    v = res[r][c]
                    if v in mapping:
                        res[r][c] = mapping[v]
    return res