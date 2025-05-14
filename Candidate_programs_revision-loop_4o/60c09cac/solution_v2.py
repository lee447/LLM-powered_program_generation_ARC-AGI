def solve(grid):
    def expand_row(row):
        expanded = []
        for value in row:
            expanded.extend([value] * 2)
        return expanded

    expanded_grid = []
    for row in grid:
        expanded_row_1 = expand_row(row)
        expanded_row_2 = expand_row(row)
        expanded_grid.append(expanded_row_1)
        expanded_grid.append(expanded_row_2)

    return expanded_grid