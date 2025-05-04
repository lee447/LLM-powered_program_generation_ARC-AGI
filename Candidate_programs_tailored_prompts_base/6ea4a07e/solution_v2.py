def solve(grid):
    colors = {cell for row in grid for cell in row if cell != 0}
    if not colors:
        return grid
    mapping = {8: 2, 3: 1, 5: 4}
    rep = mapping[colors.pop()]
    return [[0 if cell else rep for cell in row] for row in grid]