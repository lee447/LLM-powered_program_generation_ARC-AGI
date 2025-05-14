def solve(grid):
    color_count = {}
    for row in grid:
        for color in row:
            if color != 0:
                if color in color_count:
                    color_count[color] += 1
                else:
                    color_count[color] = 1
    min_color = min(color_count, key=color_count.get)
    return [[min_color, min_color], [min_color, min_color]]