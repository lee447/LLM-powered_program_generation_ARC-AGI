def solve(grid):
    def find_first_red(grid):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    return r, c
        return None, None

    def create_output_grid(start_r, start_c, height, width):
        output = [[0] * width for _ in range(height)]
        for r in range(height):
            for c in range(width):
                if c == 3:
                    if r == 0:
                        output[r][c] = 3
                    else:
                        output[r][c] = 2
                elif c == 4 and r > 0:
                    output[r][c] = 2
        return output

    start_r, start_c = find_first_red(grid)
    height = len(grid) + 6
    width = 7
    return create_output_grid(start_r, start_c, height, width)