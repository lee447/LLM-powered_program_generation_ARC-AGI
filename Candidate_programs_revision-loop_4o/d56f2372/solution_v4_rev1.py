def solve(grid):
    def extract_largest_non_zero_block(grid):
        max_area = 0
        best_block = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    min_row, max_row, min_col, max_col = r, r, c, c
                    for rr in range(r, len(grid)):
                        for cc in range(c, len(grid[0])):
                            if grid[rr][cc] != 0:
                                min_row = min(min_row, rr)
                                max_row = max(max_row, rr)
                                min_col = min(min_col, cc)
                                max_col = max(max_col, cc)
                                area = (max_row - min_row + 1) * (max_col - min_col + 1)
                                if area > max_area:
                                    max_area = area
                                    best_block = (min_row, max_row, min_col, max_col)
        return best_block

    min_row, max_row, min_col, max_col = extract_largest_non_zero_block(grid)
    result = []
    for r in range(min_row, max_row + 1):
        result.append(grid[r][min_col:max_col + 1])
    return result