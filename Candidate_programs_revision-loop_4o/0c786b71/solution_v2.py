def solve(grid):
    def mirror_and_expand(row):
        return row + row[::-1]

    def expand_grid(grid):
        expanded = []
        for row in grid:
            expanded.append(mirror_and_expand(row))
        return expanded

    def mirror_vertically(grid):
        return grid + grid[::-1]

    expanded_grid = expand_grid(grid)
    final_grid = mirror_vertically(expanded_grid)
    return final_grid