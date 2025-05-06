def solve(grid):
    g180 = [row[::-1] for row in grid[::-1]]
    top = [r + r[::-1] for r in g180]
    return top + top[::-1]