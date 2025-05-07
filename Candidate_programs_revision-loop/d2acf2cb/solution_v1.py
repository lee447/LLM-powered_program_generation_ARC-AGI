def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    mapping = {0: 8, 8: 0, 6: 7, 7: 6}
    res = [row[:] for row in grid]
    for r in range(h):
        if grid[r][0] == 4 and grid[r][w-1] == 4:
            for c in range(1, w-1):
                v = grid[r][c]
                if v in mapping:
                    res[r][c] = mapping[v]
    for c in range(w):
        if grid[0][c] == 4 and grid[h-1][c] == 4:
            for r in range(1, h-1):
                v = grid[r][c]
                if v in mapping:
                    res[r][c] = mapping[v]
    return res