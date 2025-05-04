def solve(grid):
    h = len(grid)
    w = len(grid[0])
    points = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    if len(points) < 2:
        return [row[:] for row in grid]
    points.sort()
    dr = points[1][0] - points[0][0]
    dc = points[1][1] - points[0][1]
    pts = set(points)
    start = next((p for p in points if (p[0] - dr, p[1] - dc) not in pts), points[0])
    result = [row[:] for row in grid]
    t = 0
    while True:
        r = start[0] + t * dr
        c = start[1] + t * dc
        if r < 0 or r >= h or c < 0 or c >= w:
            break
        if (r, c) not in pts:
            result[r][c] = 2
        t += 1
    return result