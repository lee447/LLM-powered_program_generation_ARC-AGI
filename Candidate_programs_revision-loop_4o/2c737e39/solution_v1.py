def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                if r + 1 < rows and grid[r + 1][c] == 0:
                    for i in range(c, cols):
                        if grid[r][i] != 0:
                            grid[r + 1][i] = grid[r][i]
                        else:
                            break
    return grid