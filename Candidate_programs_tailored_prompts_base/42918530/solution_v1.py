from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_rows = [r for r in range(H) if all(grid[r][c] == 0 for c in range(W))]
    bands = []
    for i in range(len(zero_rows) - 1):
        start = zero_rows[i] + 1
        end = zero_rows[i+1] - 1
        if end >= start:
            bands.append((start, end))
    target = len(bands) // 2
    r0, r1 = bands[target]
    zero_cols = [c for c in range(W) if all(grid[r][c] == 0 for r in range(H))]
    blocks = []
    for i in range(len(zero_cols) - 1):
        c0 = zero_cols[i] + 1
        c1 = zero_cols[i+1] - 1
        if c1 >= c0:
            blocks.append((c0, c1))
    c0, c1 = blocks[0]
    color = grid[r0][c0]
    center = (c0 + c1) // 2
    out = [row[:] for row in grid]
    height = r1 - r0 + 1
    mid = height // 2
    for dr in range(height):
        r = r0 + dr
        if dr == 0 or dr == height - 1:
            continue
        if dr == mid:
            for c in range(c0, c1+1):
                out[r][c] = color
        else:
            for c in range(c0, c1+1):
                out[r][c] = color if c == center else 0
    return out