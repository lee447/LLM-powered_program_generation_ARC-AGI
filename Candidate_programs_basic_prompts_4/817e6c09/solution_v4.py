from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    blocks = []
    for r in range(R-1):
        for c in range(C-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                blocks.append((c, r))
    blocks.sort()
    parity = 1 - (C % 2)
    out = [row[:] for row in grid]
    for i, (c, r) in enumerate(blocks):
        if i % 2 == parity:
            out[r][c] = out[r][c+1] = out[r+1][c] = out[r+1][c+1] = 8
    return out