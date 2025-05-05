def solve(grid):
    h = len(grid)
    w = len(grid[0])
    cycle = 6
    pattern = [[None] * w for _ in range(cycle)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                pattern[r % cycle][c] = v
    return [
        [
            grid[r][c] if grid[r][c] != 0 else pattern[r % cycle][c]
            for c in range(w)
        ]
        for r in range(h)
    ]