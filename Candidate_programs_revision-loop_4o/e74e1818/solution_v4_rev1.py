def solve(grid):
    import numpy as np
    grid = np.array(grid)
    non_zero_rows = [i for i in range(len(grid)) if np.any(grid[i] != 0)]
    non_zero_cols = [j for j in range(len(grid[0])) if np.any(grid[:, j] != 0)]
    new_grid = np.zeros_like(grid)
    for i, row in enumerate(non_zero_rows):
        for j, col in enumerate(non_zero_cols):
            new_grid[i, j] = grid[row, col]
    return new_grid.tolist()