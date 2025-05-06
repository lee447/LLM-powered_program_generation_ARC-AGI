from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    block_rows = {r for r in range(n) for c in range(m) if grid[r][c] != 0}
    block_cols = {c for r in range(n) for c in range(m) if grid[r][c] != 0}
    min_r, max_r = min(block_rows), max(block_rows)
    min_c, max_c = min(block_cols), max(block_cols)
    inner_rows = {r for r in range(min_r + 1, max_r) if r not in block_rows}
    inner_cols = {c for c in range(min_c + 1, max_c) if c not in block_cols}
    out = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if grid[r][c] != 0:
                out[r][c] = grid[r][c]
            elif r in inner_rows:
                out[r][c] = 2 if min_c <= c <= max_c else 1
            elif c in inner_cols:
                out[r][c] = 2 if min_r <= r <= max_r else 1
            else:
                out[r][c] = 0
    return out