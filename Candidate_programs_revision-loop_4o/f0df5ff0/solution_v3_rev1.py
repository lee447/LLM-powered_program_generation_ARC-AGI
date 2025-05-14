def solve(grid):
    def fill_ones(r, c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
            grid[r][c] = 1
            fill_ones(r + 1, c)
            fill_ones(r - 1, c)
            fill_ones(r, c + 1)
            fill_ones(r, c - 1)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fill_ones(r, c)

    return grid