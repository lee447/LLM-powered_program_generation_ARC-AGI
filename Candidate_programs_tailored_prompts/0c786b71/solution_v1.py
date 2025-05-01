def solve(grid):
    r = len(grid)
    ep = [row[::-1] + row[:] for row in grid]
    top = ep[::-1]
    return top + top[::-1]