def solve(grid):
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    color_map = [2, 7, 1, 8, 4]
    color_index = 0
    for r in range(rows):
        if all(grid[r][c] == 3 for c in range(cols)):
            output[r] = grid[r][:]
            color_index = (color_index + 1) % len(color_map)
        else:
            for c in range(cols):
                if grid[r][c] == 3:
                    output[r][c] = 3
                elif c < 3:
                    output[r][c] = color_map[color_index]
                elif c >= cols - 4:
                    output[r][c] = color_map[(color_index + 1) % len(color_map)]
    return output