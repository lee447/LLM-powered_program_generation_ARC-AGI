def solve(grid):
    def fill_color(r, c, color):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 3:
            grid[r][c] = color
            fill_color(r + 1, c, color)
            fill_color(r - 1, c, color)
            fill_color(r, c + 1, color)
            fill_color(r, c - 1, color)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 8:
                if r > 0 and grid[r - 1][c] == 3:
                    fill_color(r - 1, c, 0)
                if r < len(grid) - 1 and grid[r + 1][c] == 3:
                    fill_color(r + 1, c, 0)
                if c > 0 and grid[r][c - 1] == 3:
                    fill_color(r, c - 1, 0)
                if c < len(grid[0]) - 1 and grid[r][c + 1] == 3:
                    fill_color(r, c + 1, 0)
    return grid