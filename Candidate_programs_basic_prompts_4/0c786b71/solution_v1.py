def solve(grid):
    rot = [row[::-1] for row in grid[::-1]]
    top = [r + r[::-1] for r in rot]
    return top + top[::-1]