def solve(grid):
    h = len(grid)
    w = len(grid[0])
    row_has_1 = [any(cell == 1 for cell in row) for row in grid]
    row_groups = []
    i = 0
    while i < h:
        if row_has_1[i]:
            j = i
            while j < h and row_has_1[j]:
                j += 1
            row_groups.append(list(range(i, j)))
            i = j
        else:
            i += 1
    col_has_1 = [any(grid[r][c] == 1 for r in range(h)) for c in range(w)]
    col_groups = []
    j = 0
    while j < w:
        if col_has_1[j]:
            k = j
            while k < w and col_has_1[k]:
                k += 1
            col_groups.append(list(range(j, k)))
            j = k
        else:
            j += 1
    guide_cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] not in (0, 1)]
    if not guide_cells:
        return grid
    rs = [r for r, c in guide_cells]
    cs = [c for r, c in guide_cells]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    G = [[grid[r0 + i][c0 + j] for j in range(c1 - c0 + 1)] for i in range(r1 - r0 + 1)]
    res = [row[:] for row in grid]
    for i, rg in enumerate(row_groups):
        for j, cg in enumerate(col_groups):
            if i < len(G) and j < len(G[0]):
                val = G[i][j]
                if val != 0:
                    for r in rg:
                        for c in cg:
                            if grid[r][c] == 1:
                                res[r][c] = val
    return res