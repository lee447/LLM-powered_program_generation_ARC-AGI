def solve(grid):
    h = len(grid)
    w = len(grid[0])
    pts = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2:
                pts.append((i, j))
    (x1, y1), (x2, y2) = pts
    dx = 0 if x2 == x1 else (1 if x2 > x1 else -1)
    dy = 0 if y2 == y1 else (1 if y2 > y1 else -1)
    res = [row[:] for row in grid]
    i, j = x1, y1
    while True:
        res[i][j] = 3 if grid[i][j] == 1 else 2
        if i == x2 and j == y2:
            break
        i += dx
        j += dy
    return res