def solve(grid):
    h = len(grid)
    w = len(grid[0])
    coords3 = [(y, x) for y in range(h) for x in range(w) if grid[y][x] == 3]
    coords6 = [(y, x) for y in range(h) for x in range(w) if grid[y][x] == 6]
    ys3 = [y for y, x in coords3]
    xs3 = [x for y, x in coords3]
    min_y3, max_y3 = min(ys3), max(ys3)
    min_x3, max_x3 = min(xs3), max(xs3)
    left6 = [x for y, x in coords6 if x < min_x3]
    right6 = [x for y, x in coords6 if x > max_x3]
    up6 = [y for y, x in coords6 if y < min_y3]
    down6 = [y for y, x in coords6 if y > max_y3]
    new_min_x = min_x3 if not left6 else max(left6) + 1
    new_max_x = max_x3 if not right6 else min(right6) - 1
    new_min_y = min_y3 if not up6 else max(up6) + 1
    new_max_y = max_y3 if not down6 else min(down6) - 1
    res = [row[:] for row in grid]
    for x in range(new_min_x, new_max_x + 1):
        if res[new_min_y][x] == 0: res[new_min_y][x] = 3
        if res[new_max_y][x] == 0: res[new_max_y][x] = 3
    for y in range(new_min_y, new_max_y + 1):
        if res[y][new_min_x] == 0: res[y][new_min_x] = 3
        if res[y][new_max_x] == 0: res[y][new_max_x] = 3
    return res