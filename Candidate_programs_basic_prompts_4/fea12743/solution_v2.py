def solve(grid):
    H = len(grid)
    W = len(grid[0])
    rows = [r for r in range(H) if any(grid[r][c] == 2 for c in range(W))]
    cols = [c for c in range(W) if any(grid[r][c] == 2 for r in range(H))]
    def groups(xs):
        gs = []
        curr = [xs[0]]
        for x in xs[1:]:
            if x == curr[-1] + 1:
                curr.append(x)
            else:
                gs.append(curr)
                curr = [x]
        gs.append(curr)
        return gs
    row_groups = groups(rows)
    col_groups = groups(cols)
    # extract block 0,0 shape and compute its count vs perimeter
    r0 = row_groups[0]
    c0 = col_groups[0]
    cells = [(r, c) for r in r0 for c in c0 if grid[r][c] == 2]
    count = len(cells)
    h = len(r0)
    w = len(c0)
    perim = 2*h + 2*w - 4
    if count == perim:
        pattern = [[2,8],[8,2],[2,3]]
    elif count > perim:
        pattern = [[8,2],[8,3],[2,2]]
    else:
        pattern = [[3,8],[2,8],[2,2]]
    out = [row[:] for row in grid]
    for i, rg in enumerate(row_groups):
        for j, cg in enumerate(col_groups):
            newc = pattern[i][j]
            for r in rg:
                for c in cg:
                    if grid[r][c] == 2:
                        out[r][c] = newc
    return out