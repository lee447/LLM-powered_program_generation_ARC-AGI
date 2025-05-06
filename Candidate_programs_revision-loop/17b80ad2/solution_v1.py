from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    for c in range(w):
        pts = [(r, grid[r][c]) for r in range(h) if grid[r][c] != 0]
        if not pts:
            continue
        rows = [r for r, _ in pts]
        cols = [v for _, v in pts]
        j = 0
        n = len(rows)
        for r in range(h):
            while j < n and rows[j] <= r:
                j += 1
            if res[r][c] == 0:
                if j < n:
                    res[r][c] = cols[j]
                else:
                    res[r][c] = cols[-1]
    return res