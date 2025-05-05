def solve(grid):
    h = len(grid)
    w = len(grid[0])
    block_r = []
    block_c = []
    for i in range(h - 1):
        for j in range(w - 1):
            if grid[i][j] == 0 and grid[i][j + 1] == 0 and grid[i + 1][j] == 0 and grid[i + 1][j + 1] == 0:
                block_r = [i, i + 1]
                block_c = [j, j + 1]
                break
        if block_r:
            break
    if block_r[0] >= h / 2:
        for r in range(h):
            for c in block_c:
                grid[r][c] = 0
    else:
        for r in block_r:
            for c in range(w):
                grid[r][c] = 0
    return grid