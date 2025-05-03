def solve(grid):
    h = len(grid)
    w = len(grid[0])
    blues = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                blues.append((i, j))
    blues.sort()
    (r0, c0), (r1, c1), (r2, c2) = blues
    dr = r1 - r0
    dc = c1 - c0
    result = [row[:] for row in grid]
    r, c = r2 + dr, c2 + dc
    while 0 <= r < h and 0 <= c < w:
        result[r][c] = 2
        r += dr
        c += dc
    return result