def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    threes = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3]
    if not threes:
        return [row[:] for row in grid]
    rs = [r for r, c in threes]
    cs = [c for r, c in threes]
    min_r, max_r, min_c, max_c = min(rs), max(rs), min(cs), max(cs)
    anchors = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 6]
    above = [r for r, c in anchors if r < min_r]
    new_top = max(above) + 1 if above else min_r
    below = [r for r, c in anchors if r > max_r]
    new_bottom = min(below) - 1 if below else max_r
    lefts = [c for r, c in anchors if c < min_c]
    new_left = max(lefts) + 1 if lefts else min_c
    rights = [c for r, c in anchors if c > max_c]
    new_right = min(rights) - 1 if rights else max_c
    new_grid = [row[:] for row in grid]
    for r, c in threes:
        if r == min_r or r == max_r or c == min_c or c == max_c:
            new_grid[r][c] = 0
    for c in range(new_left, new_right + 1):
        if new_grid[new_top][c] == 0:
            new_grid[new_top][c] = 3
        if new_grid[new_bottom][c] == 0:
            new_grid[new_bottom][c] = 3
    for r in range(new_top, new_bottom + 1):
        if new_grid[r][new_left] == 0:
            new_grid[r][new_left] = 3
        if new_grid[r][new_right] == 0:
            new_grid[r][new_right] = 3
    div_cols = [c for c in range(min_c + 1, max_c) if all(grid[r][c] == 3 for r in range(min_r, max_r + 1))]
    if div_cols:
        dc = div_cols[0]
        for r in range(new_top, new_bottom + 1):
            if new_grid[r][dc] == 0:
                new_grid[r][dc] = 3
    return new_grid