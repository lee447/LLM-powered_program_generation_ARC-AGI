def solve(grid):
    R, C = len(grid), len(grid[0])
    minr, maxr, minc, maxc = R, -1, C, -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                if i < minr: minr = i
                if i > maxr: maxr = i
                if j < minc: minc = j
                if j > maxc: maxc = j
    if maxr < 0:
        return [row[:] for row in grid]
    out = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if minr <= i <= maxr or minc <= j <= maxc:
                out[i][j] = grid[i][j] if grid[i][j] == 2 else 0
            else:
                out[i][j] = grid[i][j]
    return out