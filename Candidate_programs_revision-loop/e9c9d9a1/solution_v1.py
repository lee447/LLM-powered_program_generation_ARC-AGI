from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0]) if H else 0
    sep_rows = [i for i in range(H) if all(grid[i][j] == 3 for j in range(W))]
    sep_cols = [j for j in range(W) if all(grid[i][j] == 3 for i in range(H))]
    block_rows = []
    prev = -1
    for i in sorted(sep_rows):
        if i > prev + 1:
            block_rows.append((prev + 1, i))
        prev = i
    if prev < H - 1:
        block_rows.append((prev + 1, H))
    block_cols = []
    prev = -1
    for j in sorted(sep_cols):
        if j > prev + 1:
            block_cols.append((prev + 1, j))
        prev = j
    if prev < W - 1:
        block_cols.append((prev + 1, W))
    R = len(block_rows)
    C = len(block_cols)
    res = [row[:] for row in grid]
    for i, (r0, r1) in enumerate(block_rows):
        for j, (c0, c1) in enumerate(block_cols):
            do = False
            color = None
            if i == 0 or i == R - 1:
                if j == 0:
                    do = True
                    color = 2 if i == 0 else 1
                if j == C - 1:
                    do = True
                    color = 4 if i == 0 else 8
            else:
                if 0 < j < C - 1:
                    do = True
                    color = 7
            if do:
                for r in range(r0, r1):
                    for c in range(c0, c1):
                        if grid[r][c] != 3:
                            res[r][c] = color
    return res