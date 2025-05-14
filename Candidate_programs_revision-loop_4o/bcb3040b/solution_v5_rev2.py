def solve(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                if r + 1 < rows and grid[r + 1][c] == 0:
                    new_grid[r + 1][c] = 2
                if c + 1 < cols and grid[r][c + 1] == 0:
                    new_grid[r][c + 1] = 2
                if r + 1 < rows and c + 1 < cols and grid[r + 1][c + 1] == 0:
                    new_grid[r + 1][c + 1] = 3
            elif grid[r][c] == 3:
                new_grid[r][c] = 3
            else:
                new_grid[r][c] = grid[r][c]
    for r in range(rows):
        for c in range(cols):
            if new_grid[r][c] == 0 and grid[r][c] != 0:
                new_grid[r][c] = grid[r][c]
    return new_grid