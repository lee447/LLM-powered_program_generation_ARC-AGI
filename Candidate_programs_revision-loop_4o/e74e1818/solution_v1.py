def solve(grid):
    def find_non_zero_row(grid, start_row):
        for r in range(start_row, len(grid)):
            if any(grid[r]):
                return r
        return -1

    def find_non_zero_col(grid, start_col):
        for c in range(start_col, len(grid[0])):
            if any(row[c] for row in grid):
                return c
        return -1

    def swap_rows(grid, r1, r2):
        grid[r1], grid[r2] = grid[r2], grid[r1]

    def swap_cols(grid, c1, c2):
        for row in grid:
            row[c1], row[c2] = row[c2], row[c1]

    def process_grid(grid):
        r = 0
        while r < len(grid):
            r1 = find_non_zero_row(grid, r)
            if r1 == -1:
                break
            swap_rows(grid, r, r1)
            c = 0
            while c < len(grid[0]):
                c1 = find_non_zero_col(grid, c)
                if c1 == -1:
                    break
                swap_cols(grid, c, c1)
                c += 1
            r += 1
        return grid

    return process_grid([row[:] for row in grid])