def solve(grid):
    Htot = len(grid)
    Wtot = len(grid[0])
    X = None
    for r in range(Htot):
        for c in range(Wtot):
            if grid[r][c] != 0:
                X = grid[r][c]
                break
        if X is not None:
            break
    rmin = Htot; rmax = -1; cmin = Wtot; cmax = -1
    for r in range(Htot):
        for c in range(Wtot):
            if grid[r][c] == X:
                if r < rmin: rmin = r
                if r > rmax: rmax = r
                if c < cmin: cmin = c
                if c > cmax: cmax = c
    H = rmax - rmin + 1
    W = cmax - cmin + 1
    if H % 2 == 1:
        cycle = [0, -1, 0, 1]
    else:
        if W % 2 == 0:
            cycle = [-1, 0, 1, 0]
        else:
            cycle = [1, 0, -1, 0]
    out = [[0]*Wtot for _ in range(Htot)]
    for r in range(rmin, rmax+1):
        i = r - rmin
        s = cycle[i % 4]
        for c in range(cmin, cmax+1):
            if grid[r][c] == X:
                out[r][c + s] = X
    return out