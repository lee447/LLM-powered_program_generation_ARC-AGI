def solve(grid):
    H, W = len(grid), len(grid[0])
    rs = []
    cs = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0:
                rs.append(r)
                cs.append(c)
    if not rs:
        return grid
    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)
    height = max_r - min_r + 1
    width = max_c - min_c + 1
    res = [row[:] for row in grid]
    if height > width:
        row = (min_r + max_r + 1) // 2
        for c in range(W):
            res[row][c] = 3
    else:
        col = (min_c + max_c + 1) // 2
        for r in range(H):
            res[r][col] = 3
    return res