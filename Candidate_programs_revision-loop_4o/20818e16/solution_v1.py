def solve(grid):
    def find_non_background_color(row):
        for color in row:
            if color != background_color:
                return color
        return None

    def extract_subgrid(start_row, start_col, end_row, end_col):
        return [row[start_col:end_col] for row in grid[start_row:end_row]]

    def find_color_blocks():
        color_blocks = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != background_color:
                    color_blocks.append((r, c, grid[r][c]))
        return color_blocks

    def determine_output_dimensions():
        color_blocks = find_color_blocks()
        min_r = min(r for r, c, color in color_blocks)
        max_r = max(r for r, c, color in color_blocks)
        min_c = min(c for r, c, color in color_blocks)
        max_c = max(c for r, c, color in color_blocks)
        return min_r, max_r + 1, min_c, max_c + 1

    background_color = grid[0][0]
    min_r, max_r, min_c, max_c = determine_output_dimensions()
    subgrid = extract_subgrid(min_r, min_c, max_r, max_c)

    def rotate_subgrid(subgrid):
        return [list(row) for row in zip(*subgrid[::-1])]

    rotated_subgrid = rotate_subgrid(subgrid)
    return rotated_subgrid