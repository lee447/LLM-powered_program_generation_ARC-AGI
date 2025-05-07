def solve(grid):
    R, C = len(grid), len(grid[0])
    reds = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 2]
    yellows = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 4]
    def dist_sum(y):
        return sum(abs(r - y[0]) + abs(c - y[1]) for r, c in reds)
    ref = min(yellows, key=dist_sum)
    offs = [(r - ref[0], c - ref[1]) for r, c in reds]
    out = [row[:] for row in grid]
    for y in yellows:
        if y == ref: continue
        for dr, dc in offs:
            rr, cc = y[0] + dr, y[1] + dc
            if 0 <= rr < R and 0 <= cc < C and out[rr][cc] == 0:
                out[rr][cc] = 2
    return out