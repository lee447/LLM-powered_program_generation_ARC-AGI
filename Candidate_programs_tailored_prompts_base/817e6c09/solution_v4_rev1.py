import numpy as np

def solve(grid):
    H, W = len(grid), len(grid[0])
    blocks = [(r, c) for r in range(H-1) for c in range(W-1)
              if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2]
    if not blocks:
        return [row[:] for row in grid]
    diffs = [c - r for r, c in blocks]
    side = 1 if sum(d > 0 for d in diffs) >= sum(d < 0 for d in diffs) else -1
    to_fill = []
    s = set(blocks)
    for r, c in blocks:
        if side == 1:
            if (r-1, c+1) not in s:
                to_fill.append((r, c))
        else:
            if (r-1, c-1) not in s:
                to_fill.append((r, c))
    out = [row[:] for row in grid]
    for r, c in to_fill:
        out[r][c] = out[r][c+1] = out[r+1][c] = out[r+1][c+1] = 8
    return out