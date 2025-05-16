def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    centers = []
    for r in range(h):
        for c in range(1, w-1):
            if grid[r][c] == 7 and grid[r][c-1] == 7 and grid[r][c+1] == 7:
                centers.append((r, c))
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 7:
                out[r][c] = 8
    for r, c in centers:
        for dr in (-1, 0, 1):
            rr = r + dr
            if 0 <= rr < h:
                out[rr][c] = 6
    return out