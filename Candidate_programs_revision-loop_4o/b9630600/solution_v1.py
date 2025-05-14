def solve(grid):
    def fill_horizontal(row, start, end):
        for i in range(start, end):
            row[i] = 3

    def fill_vertical(grid, col, start, end):
        for i in range(start, end):
            grid[i][col] = 3

    def process_grid(grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 3:
                    if r > 0 and grid[r-1][c] == 3:
                        fill_horizontal(grid[r], c, len(grid[0]))
                    if c > 0 and grid[r][c-1] == 3:
                        fill_vertical(grid, c, r, len(grid))
        return grid

    return process_grid([row[:] for row in grid])