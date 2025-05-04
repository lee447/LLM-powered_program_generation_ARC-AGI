from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    row_stripes = [i for i in range(H) if grid[i][0] != 0 and all(grid[i][j] == grid[i][0] for j in range(W))]
    col_stripes = [j for j in range(W) if grid[0][j] != 0 and all(grid[i][j] == grid[0][j] for i in range(H))]
    row_stripes.sort(); col_stripes.sort()
    rsegs, prev = [], 0
    for i in row_stripes:
        if prev < i: rsegs.append((prev, i))
        prev = i + 1
    if prev < H: rsegs.append((prev, H))
    csegs, prev = [], 0
    for j in col_stripes:
        if prev < j: csegs.append((prev, j))
        prev = j + 1
    if prev < W: csegs.append((prev, W))
    intr_rows = rsegs[1:-1]
    intr_cols = csegs[1:-1]
    if len(intr_cols) != 2:
        return res
    c1_0, c1_1 = intr_cols[0]
    c2_0, c2_1 = intr_cols[1]
    for r0, r1 in intr_rows:
        cells1 = [(r, c) for r in range(r0, r1) for c in range(c1_0, c1_1) if grid[r][c] != 0]
        cells2 = [(r, c) for r in range(r0, r1) for c in range(c2_0, c2_1) if grid[r][c] != 0]
        if cells1 and not cells2:
            src, dst = cells1, c2_0 - c1_0
        elif cells2 and not cells1:
            src, dst = cells2, c1_0 - c2_0
        else:
            continue
        color = grid[src[0][0]][src[0][1]]
        for r, c in src:
            res[r][c + dst] = color
    return res