from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0]) if n else 0
    blues = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 1]
    blues.sort()
    dr = blues[1][0] - blues[0][0]
    dc = blues[1][1] - blues[0][1]
    out = [row[:] for row in grid]
    r, c = blues[-1][0] + dr, blues[-1][1] + dc
    while 0 <= r < n and 0 <= c < m:
        out[r][c] = 2
        r += dr
        c += dc
    return out