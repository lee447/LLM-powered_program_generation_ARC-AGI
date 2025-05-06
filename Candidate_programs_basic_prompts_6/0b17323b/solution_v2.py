from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0])
    ones = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 1]
    if len(ones) < 2:
        return [row[:] for row in grid]
    ones_sorted = sorted(ones)
    rows = sorted(r for r, c in ones_sorted)
    cols = sorted(c for r, c in ones_sorted)
    drow = min(rows[i+1] - rows[i] for i in range(len(rows) - 1))
    dcol = min(cols[i+1] - cols[i] for i in range(len(cols) - 1))
    r, c = ones_sorted[0]
    res = [row[:] for row in grid]
    while 0 <= r < n and 0 <= c < m:
        if res[r][c] == 0:
            res[r][c] = 2
        r += drow
        c += dcol
    return res