def solve(grid):
    def clear_borders(grid):
        for i in range(len(grid)):
            grid[i][0] = 0
            grid[i][-1] = 0
        for j in range(len(grid[0])):
            grid[0][j] = 0
            grid[-1][j] = 0

    def fill_with_color(grid, color):
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    grid[i][j] = color

    clear_borders(grid)
    fill_with_color(grid, 2)
    return grid