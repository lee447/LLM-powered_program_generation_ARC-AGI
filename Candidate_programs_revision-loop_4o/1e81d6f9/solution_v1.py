def solve(grid):
    for row in grid:
        if 2 in row:
            row[row.index(2)] = 0
        if 4 in row:
            row[row.index(4)] = 0
    return grid