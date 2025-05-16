def solve(grid):
    R, C = len(grid), len(grid[0])
    r0 = R
    r1 = -1
    c0 = C
    c1 = -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 8:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    if r0 >= h:
        return [row[c0:c0+w] for row in grid[r0-h:r0]]
    else:
        return [row[c0-w:c0] for row in grid[r0:r0+h]]