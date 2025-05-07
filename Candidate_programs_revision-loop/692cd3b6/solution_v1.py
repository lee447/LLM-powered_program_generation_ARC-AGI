def solve(grid):
    h, w = len(grid), len(grid[0])
    fives = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    (r1, c1), (r2, c2) = fives
    top = min(r1, r2)
    bot = max(r1, r2)
    left = min(c1, c2)
    right = max(c1, c2)
    for r in range(top, bot + 1):
        for c in range(left, right + 1):
            if grid[r][c] == 0:
                grid[r][c] = 4
    return grid