def solve(grid):
    mapping = {8: 2, 3: 1, 5: 4}
    colors = {v for row in grid for v in row if v != 0}
    key = next(iter(colors)) if colors else 0
    new_color = mapping.get(key, 0)
    result = []
    for row in grid:
        new_row = []
        for v in row:
            new_row.append(0 if v != 0 else new_color)
        result.append(new_row)
    return result