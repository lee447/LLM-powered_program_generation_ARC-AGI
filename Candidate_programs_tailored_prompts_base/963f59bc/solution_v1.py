from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    rows = {}
    for r, c in ones:
        rows.setdefault(r, 0)
        rows[r] += 1
    single_rows = [r for r, cnt in rows.items() if cnt == 1]
    anchor_r = max(single_rows)
    anchor_c = next(c for r, c in ones if r == anchor_r)
    offsets = [(r - anchor_r, c - anchor_c) for r, c in ones]
    others = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] not in (0, 1)]
    for r0, c0, col in others:
        for dr, dc in offsets:
            r1, c1 = r0 + dr, c0 + dc
            if 0 <= r1 < h and 0 <= c1 < w and out[r1][c1] != 1:
                out[r1][c1] = col
    return out