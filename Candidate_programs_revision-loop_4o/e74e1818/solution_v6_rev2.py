def solve(grid):
    import numpy as np
    grid = np.array(grid)
    new_grid = np.zeros_like(grid)
    for row in range(len(grid)):
        non_zero_indices = np.where(grid[row] != 0)[0]
        if len(non_zero_indices) > 0:
            start, end = non_zero_indices[0], non_zero_indices[-1]
            new_grid[row, start:end+1] = grid[row, start:end+1]
    return new_grid.tolist()