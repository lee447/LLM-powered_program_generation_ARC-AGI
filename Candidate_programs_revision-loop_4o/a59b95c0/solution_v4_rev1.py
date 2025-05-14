def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = []
    for row in grid:
        new_row = row * (12 // m)
        result.append(new_row)
    result *= (12 // n)
    return result