def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 6:
                if c + 1 < cols and grid[r][c + 1] == 6:
                    if c + 2 < cols and grid[r][c + 2] == 6:
                        grid[r][c + 1] = 4
                        grid[r][c + 2] = 4
                    else:
                        grid[r][c + 1] = 4
                elif c + 1 < cols and grid[r][c + 1] == 4:
                    if c + 2 < cols and grid[r][c + 2] == 4:
                        grid[r][c + 1] = 4
                        grid[r][c + 2] = 4
    return grid