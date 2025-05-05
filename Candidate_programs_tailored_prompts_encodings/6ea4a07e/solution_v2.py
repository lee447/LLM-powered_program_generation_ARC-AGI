def solve(grid):
    mapping = {8: 2, 3: 1, 5: 4}
    h, w = len(grid), len(grid[0])
    input_color = next(c for row in grid for c in row if c != 0)
    out_color = mapping[input_color]
    return [[0 if grid[i][j] != 0 else out_color for j in range(w)] for i in range(h)]