def solve(grid):
    n = len(grid)
    new_grid = [row[:] for row in grid]
    blue_inds = [i for i in range(min(n, len(grid[0]))) if grid[i][i] == 1]
    if len(blue_inds) < 2:
        return new_grid
    gap = blue_inds[1] - blue_inds[0]
    last = blue_inds[-1]
    idx = last + gap
    while idx < min(n, len(grid[0])):
        if new_grid[idx][idx] != 1:
            new_grid[idx][idx] = 2
        idx += gap
    return new_grid