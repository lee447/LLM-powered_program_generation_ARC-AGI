def solve(grid):
    H, W = len(grid), len(grid[0])
    row_walls = [r for r in range(H) if all(grid[r][c] == 4 for c in range(W))]
    col_walls = [c for c in range(W) if all(grid[r][c] == 4 for r in range(H))]
    row_bounds = [-1] + row_walls + [H]
    col_bounds = [-1] + col_walls + [W]
    rooms = []
    for i in range(len(row_bounds) - 1):
        r0 = row_bounds[i] + 1
        r1 = row_bounds[i+1] - 1
        if r0 > r1: continue
        for j in range(len(col_bounds) - 1):
            c0 = col_bounds[j] + 1
            c1 = col_bounds[j+1] - 1
            if c0 > c1: continue
            rooms.append((r0, r1, c0, c1))
    master = None
    for r0, r1, c0, c1 in rooms:
        s = {grid[r][c] for r in range(r0, r1+1) for c in range(c0, c1+1)}
        nz = s - {0}
        if len(nz) == 1 and 1 not in nz:
            master = (r0, r1, c0, c1, nz.pop())
            break
    if master is None:
        return grid
    r0, r1, c0, c1, col = master
    h, w = r1 - r0 + 1, c1 - c0 + 1
    mask = [[grid[r0+i][c0+j] == col for j in range(w)] for i in range(h)]
    out = [row[:] for row in grid]
    for rr0, rr1, cc0, cc1 in rooms:
        s = {out[r][c] for r in range(rr0, rr1+1) for c in range(cc0, cc1+1)}
        if s <= {0, 1} and 1 in s:
            for i in range(rr1 - rr0 + 1):
                for j in range(cc1 - cc0 + 1):
                    if mask[i][j] and out[rr0+i][cc0+j] == 1:
                        out[rr0+i][cc0+j] = col
    return out