from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    clusters = [(r, c) for r in range(H-1) for c in range(W-1)
                if grid[r][c] == grid[r][c+1] == grid[r+1][c] == grid[r+1][c+1] == 2]
    cols = sorted({c for _, c in clusters})
    n = len(cols)
    start = 0 if n % 2 else 1
    sel = set(cols[i] for i in range(start, n, 2))
    for r, c in clusters:
        if c in sel:
            out[r][c] = out[r][c+1] = out[r+1][c] = out[r+1][c+1] = 8
    return out