def solve(grid):
    def find_bounds():
        min_row, max_row = len(grid), -1
        min_col, max_col = len(grid[0]), -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 3:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return min_row, max_row, min_col, max_col

    min_row, max_row, min_col, max_col = find_bounds()

    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if grid[r][c] != 3:
                grid[r][c] = 0

    for r in range(min_row, max_row + 1):
        grid[r][min_col] = 3
        grid[r][max_col] = 3

    for c in range(min_col, max_col + 1):
        grid[min_row][c] = 3
        grid[max_row][c] = 3

    return grid