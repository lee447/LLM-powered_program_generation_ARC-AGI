def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = []
    for row in grid:
        new_row = row * (6 // m)
        result.append(new_row)
    result *= (6 // n)
    return result