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
                color = row[start]
                fill_row(row, start, end, color)

        for j in range(len(grid[0])):
            col = [grid[i][j] for i in range(len(grid))]
            segments = find_non_zero_segments(col)
            for start, end in segments:
                color = col[start]
                fill_column(grid, j, start, end, color)

    def fill_diagonals(grid):
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    color = grid[i][j]
                    x, y = i, j
                    while x < n and y < m and grid[x][y] == 0:
                        grid[x][y] = color
                        x += 1
                        y += 1
                    x, y = i, j
                    while x < n and y >= 0 and grid[x][y] == 0:
                        grid[x][y] = color
                        x += 1
                        y -= 1

    output_grid = [row[:] for row in grid]
    process_grid(output_grid)
    fill_diagonals(output_grid)
    return output_grid