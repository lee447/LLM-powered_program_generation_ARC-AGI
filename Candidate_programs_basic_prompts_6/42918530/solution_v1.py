from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    zero_rows = [r for r in range(h) if all(grid[r][c] == 0 for c in range(w))]
    block_rows = [zero_rows[i] + 1 for i in range(len(zero_rows) - 1)]
    zero_cols = [c for c in range(w) if all(grid[r][c] == 0 for r in range(h))]
    block_cols = [zero_cols[j] + 1 for j in range(len(zero_cols) - 1)]
    block_h = block_rows[1] - zero_rows[0] - 1 if len(block_rows) > 1 else h - zero_rows[0] - 1
    block_w = block_cols[1] - zero_cols[0] - 1 if len(block_cols) > 1 else w - zero_cols[0] - 1
    out = [row[:] for row in grid]
    r0 = block_rows[-1]
    c0 = block_cols[0]
    color = grid[r0][c0 + 1]
    mid_r = r0 + block_h // 2
    mid_c = c0 + block_w // 2
    out[mid_r][mid_c] = color
    out[mid_r - 1][mid_c] = color
    out[mid_r + 1][mid_c] = color
    out[mid_r][mid_c - 1] = color
    out[mid_r][mid_c + 1] = color
    return out