from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_rows = [r for r in range(H) if all(grid[r][c] == 0 for c in range(W))]
    bands = [(zero_rows[i] + 1, zero_rows[i+1] - 1) for i in range(len(zero_rows) - 1) if zero_rows[i+1] - zero_rows[i] > 1]
    target = len(bands) // 2
    r0, r1 = bands[target]
    zero_cols = [c for c in range(W) if all(grid[r][c] == 0 for r in range(H))]
    blocks = [(zero_cols[i] + 1, zero_cols[i+1] - 1) for i in range(len(zero_cols) - 1) if zero_cols[i+1] - zero_cols[i] > 1]
    out = [row[:] for row in grid]
    height = r1 - r0 + 1
    mid = height // 2
    for c0, c1 in blocks:
        color = grid[r0][c0]
        center = (c0 + c1) // 2
        for dr in range(1, height-1):
            r = r0 + dr
            if dr == mid:
                for c in range(c0, c1+1):
                    out[r][c] = color
            else:
                out[r][center] = color
    return out