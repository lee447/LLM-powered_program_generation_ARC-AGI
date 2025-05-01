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
    pattern = None
    for pi, (r0, r1) in enumerate(row_segs):
        for pj, (c0, c1) in enumerate(col_segs):
            for r in range(r0, r1 + 1):
                for c in range(c0, c1 + 1):
                    v = grid[r][c]
                    if v not in (0, 1, 4):
                        pattern = (pi, pj, v)
                        break
                if pattern:
                    break
            if pattern:
                break
        if pattern:
            break
    pr, pc, X = pattern
    r0, r1 = row_segs[pr]
    c0, c1 = col_segs[pc]
    offsets = [(r - r0, c - c0) for r in range(r0, r1 + 1) for c in range(c0, c1 + 1) if grid[r][c] == X]
    out = [row[:] for row in grid]
    N = min(len(row_segs), len(col_segs))
    for i in range(N):
        br, er = row_segs[i]
        bc, ec = col_segs[i]
        h, w = er - br + 1, ec - bc + 1
        for dr, dc in offsets:
            if dr < h and dc < w:
                out[br + dr][bc + dc] = X
    return out