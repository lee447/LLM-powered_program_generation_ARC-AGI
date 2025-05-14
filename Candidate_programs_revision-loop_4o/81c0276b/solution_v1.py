def solve(grid):
    def extract_subgrid(grid, start_row, start_col, height, width):
        return [row[start_col:start_col + width] for row in grid[start_row:start_row + height]]

    def find_non_zero_block(grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    return row, col
        return None, None

    start_row, start_col = find_non_zero_block(grid)
    if start_row is None:
        return []

    block_height = 0
    while start_row + block_height < len(grid) and grid[start_row + block_height][start_col] != 0:
        block_height += 1

    block_width = 0
    while start_col + block_width < len(grid[0]) and grid[start_row][start_col + block_width] != 0:
        block_width += 1

    return extract_subgrid(grid, start_row, start_col, block_height, block_width)