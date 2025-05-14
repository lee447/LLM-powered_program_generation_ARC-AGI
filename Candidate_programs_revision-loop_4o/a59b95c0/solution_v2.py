def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(3):
        for row in grid:
            new_row = []
            for j in range(3):
                new_row.extend(row)
            result.append(new_row)
    return result