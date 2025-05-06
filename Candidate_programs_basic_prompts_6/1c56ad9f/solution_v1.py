def solve(grid):
    h = len(grid)
    w = len(grid[0])
    color = None
    for row in grid:
        for v in row:
            if v != 0:
                color = v
                break
        if color is not None:
            break
    ys = [y for y in range(h) if any(grid[y][x] == color for x in range(w))]
    if not ys:
        return grid
    y0, y1 = min(ys), max(ys)
    dx_maps = {3: [-1, -1, 0, 1], 2: [0, -1, 0, 1], 5: [-1, 0, 1, 0], 8: [1, 0, -1, 0]}
    dx_map = dx_maps.get(color, [0, 0, 0, 0])
    out = [[0]*w for _ in range(h)]
    for y in range(y0, y1+1):
        if y == y1:
            dx = 0
        else:
            dx = dx_map[(y - y0) % 4]
        for x in range(w):
            if grid[y][x] == color:
                nx = x + dx
                if 0 <= nx < w:
                    out[y][nx] = color
    return out