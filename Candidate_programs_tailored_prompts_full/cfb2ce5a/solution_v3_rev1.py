from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    # top quadrants
    main_vals = []
    for i in range(1, 5):
        for j in range(1, 5):
            v = grid[i][j]
            if v != 0 and v not in main_vals:
                main_vals.append(v)
    anchor_vals = []
    for i in range(1, 5):
        for j in range(5, 9):
            v = grid[i][j]
            if v != 0 and v not in anchor_vals:
                anchor_vals.append(v)
    # determine mapping by markers in col 5
    mapping = {}
    for i in range(1, 5):
        if grid[i][5] != 0:
            mapping[grid[i][4]] = grid[i][5]
    if len(main_vals) == 2 and len(anchor_vals) == 2:
        unm = [c for c in main_vals if c not in mapping]
        una = [c for c in anchor_vals if c not in mapping.values()]
        if unm and una:
            mapping[unm[0]] = una[0]
    for i in range(1, 5):
        for j in range(1, 5):
            res[i][j+4] = mapping.get(grid[i][j], 0)
    # bottom quadrants: copy input blanks and seeds only
    # bottom-left
    bl = []
    for i in range(5, 9):
        for j in range(1, 5):
            if grid[i][j] != 0 and grid[i][j] not in bl:
                bl.append((i, j, grid[i][j]))
    if len(bl) == 2:
        (i1,j1,c1),(i2,j2,c2) = bl
        for bi in range(4):
            for bj in range(4):
                res[5+bi][1+bj] = c1 if abs((5+bi)-i1)+abs((1+bj)-j1) <= abs((5+bi)-i2)+abs((1+bj)-j2) else c2
    # bottom-right
    br = []
    for i in range(5, 9):
        for j in range(5, 9):
            if grid[i][j] != 0 and grid[i][j] not in br:
                br.append((i, j, grid[i][j]))
    if len(br) == 2:
        (i1,j1,c1),(i2,j2,c2) = br
        for bi in range(4):
            for bj in range(4):
                res[5+bi][5+bj] = c1 if abs((5+bi)-i1)+abs((5+bj)-j1) <= abs((5+bi)-i2)+abs((5+bj)-j2) else c2
    return res