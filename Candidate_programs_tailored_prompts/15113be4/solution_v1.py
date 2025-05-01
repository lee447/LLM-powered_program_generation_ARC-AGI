from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    row_divs = [r for r in range(H) if all(grid[r][c] == 4 for c in range(W))]
    col_divs = [c for c in range(W) if all(grid[r][c] == 4 for r in range(H))]
    row_divs.sort()
    col_divs.sort()
    row_segs = []
    prev = -1
    for d in row_divs:
        if d - prev - 1 > 0:
            row_segs.append((prev + 1, d - 1))
        prev = d
    if H - prev - 1 > 0:
        row_segs.append((prev + 1, H - 1))
    col_segs = []
    prev = -1
    for d in col_divs:
        if d - prev - 1 > 0:
            col_segs.append((prev + 1, d - 1))
        prev = d
    if W - prev - 1 > 0:
        col_segs.append((prev + 1, W - 1))
    r0, r1 = row_segs[0]
    c0, c1 = col_segs[0]
    X = None
    offsets = []
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            v = grid[r][c]
            if v not in (0, 1, 4):
                X = v
                offsets.append((r - r0, c - c0))
    out = [row[:] for row in grid]
    for i in range(len(row_segs)):
        rs, _ = row_segs[i]
        cs, _ = col_segs[i]
        for dr, dc in offsets:
            out[rs + dr][cs + dc] = X
    return out