def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    r = 0
    while r < h:
        if all(v == 0 for v in grid[r]):
            r += 1
            continue
        start = r
        band_color = next(v for v in grid[r] if v != 0)
        r2 = r + 1
        while r2 < h and any(v != 0 for v in grid[r2]) and all(v == 0 or v == band_color for v in grid[r2]):
            r2 += 1
        end = r2 - 1
        length = end - start + 1
        if length > 1:
            for i in range(length):
                res[start + i] = grid[end - i][:]
        r = r2
    return res