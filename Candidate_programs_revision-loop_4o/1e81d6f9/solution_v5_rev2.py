def solve(grid):
    from collections import defaultdict
    color_positions = defaultdict(list)
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value != 0:
                color_positions[value].append((i, j))
    for color, positions in color_positions.items():
        if color == 5:
            for i, j in positions:
                grid[i][j] = 5
        else:
            for i, j in positions:
                grid[i][j] = 0
    return grid