from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    rows_zero = [i for i in range(H) if all(grid[i][j] == 0 for j in range(W))]
    cols_zero = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    block_rows = [(rows_zero[i] + 1, rows_zero[i+1]) for i in range(len(rows_zero) - 1)]
    block_cols = [(cols_zero[j] + 1, cols_zero[j+1]) for j in range(len(cols_zero) - 1)]
    out = [row[:] for row in grid]
    if len(block_rows) < 2:
        return out
    for bc in block_cols:
        br_src = block_rows[-1]
        r0, r1 = br_src
        c0, c1 = bc
        interior_rows = range(r0+1, r1-1)
        interior_cols = range(c0+1, c1-1)
        mask = [[grid[r][c] != 0 for c in interior_cols] for r in interior_rows]
        if not any(any(row) for row in mask):
            continue
        br_dst = block_rows[-2]
        dr0, dr1 = br_dst
        dc0, dc1 = bc
        color = grid[dr0][dc0]
        for i, r in enumerate(range(dr0+1, dr1-1)):
            for j, c in enumerate(interior_cols):
                if mask[i][j] and out[r][c] == 0:
                    out[r][c] = color
    return out