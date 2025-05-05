def solve(grid):
    R, C = len(grid), len(grid[0])
    # find top‐left of the light-blue block
    r0 = R; c0 = C
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 8:
                if i < r0: r0 = i
                if j < c0: c0 = j
    # block height
    h = 0
    while r0 + h < R and grid[r0 + h][c0] == 8:
        h += 1
    # block width
    w = 0
    while c0 + w < C and grid[r0][c0 + w] == 8:
        w += 1
    # find the first grey row above the block
    grey_r = None
    for i in range(r0 - 1, -1, -1):
        if grid[i][c0] == 5:
            grey_r = i
            break
    # find the preceding grey column on that row
    grey_c = None
    for j in range(c0 - 1, -1, -1):
        if grid[grey_r][j] == 5:
            grey_c = j
            break
    # extract the h×w slice
    out = []
    for i in range(grey_r + 1, grey_r + 1 + h):
        out.append(grid[i][grey_c + 1 : grey_c + 1 + w])
    return out