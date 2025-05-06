def solve(grid):
    rows, cols = len(grid), len(grid[0])
    threes = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c]==3]
    grays = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c]==6]
    min_r = min(r for r,c in threes)
    max_r = max(r for r,c in threes)
    min_c = min(c for r,c in threes)
    max_c = max(c for r,c in threes)
    new_min_r, new_max_r = min_r, max_r
    new_min_c, new_max_c = min_c, max_c
    for r,c in grays:
        if min_r <= r <= max_r:
            if c < min_c:
                new_min_c = min(new_min_c, c+1)
            if c > max_c:
                new_max_c = max(new_max_c, c-1)
        if min_c <= c <= max_c:
            if r < min_r:
                new_min_r = min(new_min_r, r+1)
            if r > max_r:
                new_max_r = max(new_max_r, r-1)
    out = [row[:] for row in grid]
    for c in range(new_min_c, new_max_c+1):
        out[new_min_r][c] = 3
        out[new_max_r][c] = 3
    for r in range(new_min_r, new_max_r+1):
        out[r][new_min_c] = 3
        out[r][new_max_c] = 3
    return out