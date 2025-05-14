def solve(grid):
    def extract_non_zero_block(grid):
        min_row, max_row = len(grid), 0
        min_col, max_col = len(grid[0]), 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return min_row, max_row, min_col, max_col

    min_row, max_row, min_col, max_col = extract_non_zero_block(grid)
    result = []
    for r in range(min_row, max_row + 1):
        result.append(grid[r][min_col:max_col + 1])
    return result