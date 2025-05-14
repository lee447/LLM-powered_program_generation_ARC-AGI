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

    subgrid = extract_subgrid(grid, start_row, start_col, block_height, block_width)

    def find_largest_non_zero_block(subgrid):
        max_area = 0
        best_subgrid = []
        for r in range(len(subgrid)):
            for c in range(len(subgrid[0])):
                if subgrid[r][c] != 0:
                    height = 0
                    while r + height < len(subgrid) and subgrid[r + height][c] != 0:
                        height += 1
                    width = 0
                    while c + width < len(subgrid[0]) and subgrid[r][c + width] != 0:
                        width += 1
                    area = height * width
                    if area > max_area:
                        max_area = area
                        best_subgrid = extract_subgrid(subgrid, r, c, height, width)
        return best_subgrid

    return find_largest_non_zero_block(subgrid)