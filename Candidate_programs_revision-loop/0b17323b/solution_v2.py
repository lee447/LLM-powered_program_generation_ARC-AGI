def solve(grid):
    h, w = len(grid), len(grid[0])
    ones = sorted((r, c) for r in range(h) for c in range(w) if grid[r][c] == 1)
    if len(ones) < 2:
        return [row[:] for row in grid]
    dr = ones[1][0] - ones[0][0]
    dc = ones[1][1] - ones[0][1]
    out = [row[:] for row in grid]
    r, c = ones[-1][0] + dr, ones[-1][1] + dc
    while 0 <= r < h and 0 <= c < w:
        out[r][c] = 2
        r += dr
        c += dc
    return out