def solve(grid):
    h = len(grid)
    w = len(grid[0])
    min_r, max_r = h, -1
    min_c, max_c = w, -1
    for r in range(h):
        for c, v in enumerate(grid[r]):
            if v == 8:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    N = max_r - min_r + 1
    start_c = min_c - N
    return [row[start_c:start_c+N] for row in grid[min_r:min_r+N]]