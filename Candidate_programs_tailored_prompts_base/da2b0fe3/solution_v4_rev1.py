def solve(grid):
    h = len(grid)
    w = len(grid[0])
    ys = []
    xs = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0:
                ys.append(y)
                xs.append(x)
    if not ys:
        return [row[:] for row in grid]
    min_y, max_y = min(ys), max(ys)
    min_x, max_x = min(xs), max(xs)
    res = [row[:] for row in grid]
    hy = (min_y + max_y + 1) // 2
    ok = True
    for x in range(min_x, max_x + 1):
        if grid[hy][x] != 0:
            ok = False
            break
    if ok:
        for x in range(w):
            res[hy][x] = 3
        return res
    vx = (min_x + max_x + 1) // 2
    ok = True
    for y in range(min_y, max_y + 1):
        if grid[y][vx] != 0:
            ok = False
            break
    if ok:
        for y in range(h):
            res[y][vx] = 3
    return res