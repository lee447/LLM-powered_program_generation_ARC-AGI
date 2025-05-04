def solve(grid):
    N = len({c for row in grid for c in row})
    tile = [row * N for row in grid]
    return tile * N