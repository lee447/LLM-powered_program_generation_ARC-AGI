def solve(grid):
    R, C = len(grid), len(grid[0])
    r0, r1, c0, c1 = R, -1, C, -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    return [[grid[i][C-1-j] for j in range(c0, c1+1)] for i in range(r0, r1+1)]