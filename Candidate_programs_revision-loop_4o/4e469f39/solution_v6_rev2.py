def solve(grid):
    def clear_borders(grid):
        for i in range(len(grid)):
            grid[i][0] = 0
            grid[i][-1] = 0
        for j in range(len(grid[0])):
            grid[0][j] = 0
            grid[-1][j] = 0

    def shift_rows(grid):
        for i in range(1, len(grid) - 1):
            grid[i] = [0] + grid[i][1:-1] + [0]

    def shift_columns(grid):
        for j in range(1, len(grid[0]) - 1):
            for i in range(len(grid) - 1, 0, -1):
                grid[i][j] = grid[i-1][j]
            grid[0][j] = 0

    clear_borders(grid)
    shift_rows(grid)
    shift_columns(grid)
    return grid