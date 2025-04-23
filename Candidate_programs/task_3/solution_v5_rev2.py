from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zeros_r = {i for i in range(H) if all(x == 0 for x in grid[i])}
    zeros_c = {j for j in range(W) if all(grid[i][j] == 0 for i in range(H))}
    block_rows = []
    prev = -1
    for r in sorted(zeros_r):
        if prev + 1 < r:
            block_rows.append((prev + 1, r))
        prev = r
    if prev + 1 < H:
        block_rows.append((prev + 1, H))
    block_cols = []
    prev = -1
    for c in sorted(zeros_c):
        if prev + 1 < c:
            block_cols.append((prev + 1, c))
        prev = c
    if prev + 1 < W:
        block_cols.append((prev + 1, W))
    out = [row[:] for row in grid]
    changed = True
    while changed:
        changed = False
        for r0, r1 in block_rows:
            for c0, c1 in block_cols:
                for r in range(r0 + 1, r1 - 1):
                    for c in range(c0 + 1, c1 - 1):
                        if out[r][c] == 0:
                            left = out[r][c - 1]
                            right = out[r][c + 1]
                            up = out[r - 1][c]
                            down = out[r + 1][c]
                            if left > 0 and left == right:
                                out[r][c] = left
                                changed = True
                            elif up > 0 and up == down:
                                out[r][c] = up
                                changed = True
    return out