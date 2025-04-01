from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    m = len(grid[0]) if n else 0
    has_grey = any(5 in row for row in grid)
    has_red_blue = any(any(c in (1,2) for c in row) for row in grid)
    out = [list(r) for r in grid]
    if has_grey:
        col = (m - 1) // 2
        for i in range(n):
            out[i][col] = 3
    elif has_red_blue:
        row = (n - 1) // 2
        for j in range(m):
            out[row][j] = 3
    return out