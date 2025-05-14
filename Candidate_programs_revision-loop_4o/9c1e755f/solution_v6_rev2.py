def solve(grid):
    import numpy as np
    grid = np.array(grid)
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                color = grid[r][c]
                if r + 1 < rows and grid[r + 1][c] == 0:
                    for i in range(r + 1, rows):
                        if grid[i][c] == 0:
                            grid[i][c] = color
                        else:
                            break
                if c + 1 < cols and grid[r][c + 1] == 0:
                    for j in range(c + 1, cols):
                        if grid[r][j] == 0:
                            grid[r][j] = color
                        else:
                            break
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                if r > 0 and grid[r - 1][c] != 0:
                    grid[r][c] = grid[r - 1][c]
                elif c > 0 and grid[r][c - 1] != 0:
                    grid[r][c] = grid[r][c - 1]
    return grid.tolist()