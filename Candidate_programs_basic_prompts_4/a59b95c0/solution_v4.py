def solve(grid):
    factor = len({v for row in grid for v in row})
    block = [row * factor for row in grid]
    return [r for _ in range(factor) for r in block]