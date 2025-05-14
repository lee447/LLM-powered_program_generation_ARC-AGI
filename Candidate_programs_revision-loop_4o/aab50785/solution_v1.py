def solve(grid):
    def extract_subgrid(grid, start_row, start_col, height, width):
        return [row[start_col:start_col + width] for row in grid[start_row:start_row + height]]

    def find_non_zero_subgrid(grid):
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    for h in range(1, rows - r + 1):
                        for w in range(1, cols - c + 1):
                            subgrid = extract_subgrid(grid, r, c, h, w)
                            if all(any(cell != 0 for cell in row) for row in subgrid):
                                return subgrid
        return []

    return find_non_zero_subgrid(grid)