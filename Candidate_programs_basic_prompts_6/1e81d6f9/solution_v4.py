def solve(grid):
    R, C = len(grid), len(grid[0])
    r_div = c_div = None
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 5:
                if j-1 >= 0 and i-1 >= 0 and grid[i][j-1] == 5 and grid[i-1][j] == 5:
                    r_div, c_div = i, j
                    break
        if r_div is not None:
            break
    quads = [[], [], [], []]
    for i in range(R):
        for j in range(C):
            if i == r_div or j == c_div: continue
            v = grid[i][j]
            if v != 0 and v != 5:
                if i < r_div and j < c_div:
                    quads[0].append((i, j, v))
                elif i < r_div and j > c_div:
                    quads[1].append((i, j, v))
                elif i > r_div and j < c_div:
                    quads[2].append((i, j, v))
                elif i > r_div and j > c_div:
                    quads[3].append((i, j, v))
    target = None
    for q in quads:
        if len(q) == 1:
            target = q[0]
            break
    if target is not None:
        ti, tj, tv = target
        out = [row[:] for row in grid]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == tv and not (i == ti and j == tj):
                    out[i][j] = 0
        return out
    return grid