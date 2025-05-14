def solve(grid):
    def fill_row(row, start, end, color):
        for i in range(start, end):
            row[i] = color

    def fill_column(grid, col, start, end, color):
        for i in range(start, end):
            grid[i][col] = color

    def find_non_zero_segments(row):
        segments = []
        start = None
        for i, val in enumerate(row):
            if val != 0 and start is None:
                start = i
            elif val == 0 and start is not None:
                segments.append((start, i))
                start = None
        if start is not None:
            segments.append((start, len(row)))
        return segments

    def process_grid(grid):
        for i, row in enumerate(grid):
            segments = find_non_zero_segments(row)
            for start, end in segments:
                fill_row(row, start, end, row[start])

        for j in range(len(grid[0])):
            col = [grid[i][j] for i in range(len(grid))]
            segments = find_non_zero_segments(col)
            for start, end in segments:
                fill_column(grid, j, start, end, col[start])

    def fill_surrounding(grid):
        rows, cols = len(grid), len(grid[0])
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 0:
                    neighbors = [grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]]
                    non_zero_neighbors = [n for n in neighbors if n != 0]
                    if len(set(non_zero_neighbors)) == 1:
                        grid[i][j] = non_zero_neighbors[0]

    output_grid = [row[:] for row in grid]
    process_grid(output_grid)
    fill_surrounding(output_grid)
    return output_grid