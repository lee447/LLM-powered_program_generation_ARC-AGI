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
    h, w = r1 - r0 + 1, c1 - c0 + 1
    if r0 >= h:
        block = [row[c0:c1+1] for row in grid[r0-h:r0]]
    else:
        block = [row[c0:c1+1] for row in grid[r1+1:r1+1+h]]
    return [row[::-1] for row in block[::-1]]