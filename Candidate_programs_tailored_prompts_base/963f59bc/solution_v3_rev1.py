from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    rows = {}
    for r, c in ones:
        rows.setdefault(r, []).append(c)
    single_rows = sorted([r for r, cs in rows.items() if len(cs) == 1])
    anchor_r = single_rows[-1]
    anchor_c = rows[anchor_r][0]
    minc = min(c for r, c in ones)
    drs = [r - anchor_r for r, c in ones]
    dcs = [c - minc       for r, c in ones]
    out = [row[:] for row in grid]
    for r0 in range(h):
        for c0 in range(w):
            col = grid[r0][c0]
            if col not in (0, 1):
                for dr, dc in zip(drs, dcs):
                    r1, c1 = r0 + dr, c0 + dc
                    if 0 <= r1 < h and 0 <= c1 < w and out[r1][c1] == 0:
                        out[r1][c1] = col
    return out