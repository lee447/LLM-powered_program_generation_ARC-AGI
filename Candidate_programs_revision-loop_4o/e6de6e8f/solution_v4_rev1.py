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
                if r == 0 and c == 3:
                    output[r][c] = 3
                elif r >= start_r and c >= start_c:
                    if r - start_r < len(grid) and c - start_c < len(grid[0]) and grid[r - start_r][c - start_c] == 2:
                        output[r][c] = 2
        return output

    start_r, start_c = find_first_red(grid)
    height = len(grid) + 6
    width = 7
    return create_output_grid(start_r, start_c, height, width)