def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                color = grid[r][c]
                for i in range(r, rows):
                    if grid[i][c] == 0:
                        break
                    for j in range(c, cols):
                        if grid[i][j] == 0:
                            break
                        grid[i][j] = color
    return grid