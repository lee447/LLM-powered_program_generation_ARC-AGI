import numpy as np
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    row_seps = [i for i in range(h) if all(v == 0 for v in grid[i])]
    col_seps = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    row_ranges = [(row_seps[k] + 1, row_seps[k+1] - 1) for k in range(len(row_seps)-1) if row_seps[k+1] - row_seps[k] > 1]
    col_ranges = [(col_seps[k] + 1, col_seps[k+1] - 1) for k in range(len(col_seps)-1) if col_seps[k+1] - col_seps[k] > 1]
    out = [row[:] for row in grid]
    if not row_ranges or not col_ranges:
        return out
    block_h = row_ranges[0][1] - row_ranges[0][0] + 1
    block_w = col_ranges[0][1] - col_ranges[0][0] + 1
    drs = [block_h//2 - 1, block_h//2] if block_h > 1 else [0]
    dcs = [block_w//2 - 1, block_w//2] if block_w > 1 else [0]
    for r0, r1 in row_ranges:
        c0_0 = col_ranges[0][0]
        background = grid[r0][c0_0+1] if c0_0+1 <= col_ranges[0][1] else grid[r0][c0_0]
        pos_vals = []
        for dr in drs:
            for dc in dcs:
                rr, cc = r0+dr, c0_0+dc
                pos_vals.append(((rr, cc), grid[rr][cc]))
        filtered = [(pos, v) for pos, v in pos_vals if v != background]
        vals = [v for _, v in filtered]
        if len(set(vals)) > 1:
            freq = {v: vals.count(v) for v in set(vals)}
            anchor_val = min(freq, key=lambda x: freq[x])
            for pos, v in filtered:
                if v == anchor_val:
                    r_anchor, c_anchor = pos
                    break
            dr_off = r_anchor - r0
            dc_off = c_anchor - c0_0
            for c0, _ in col_ranges[1:]:
                out[r0+dr_off][c0+dc_off] = anchor_val
    return out