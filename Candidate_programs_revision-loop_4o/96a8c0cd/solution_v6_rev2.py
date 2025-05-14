def solve(grid):
    def fill_horizontal_line(row, start_col, end_col, color):
        for col in range(start_col, end_col + 1):
            if grid[row][col] == 0:
                grid[row][col] = color

    def fill_vertical_line(start_row, end_row, col, color):
        for row in range(start_row, end_row + 1):
            if grid[row][col] == 0:
                grid[row][col] = color

    def find_horizontal_segments():
        segments = []
        for r in range(len(grid)):
            start = None
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    if start is None:
                        start = c
                else:
                    if start is not None:
                        segments.append((r, start, c - 1))
                        start = None
            if start is not None:
                segments.append((r, start, len(grid[0]) - 1))
        return segments

    def find_vertical_segments():
        segments = []
        for c in range(len(grid[0])):
            start = None
            for r in range(len(grid)):
                if grid[r][c] != 0:
                    if start is None:
                        start = r
                else:
                    if start is not None:
                        segments.append((start, r - 1, c))
                        start = None
            if start is not None:
                segments.append((start, len(grid) - 1, c))
        return segments

    horizontal_segments = find_horizontal_segments()
    vertical_segments = find_vertical_segments()

    for r, start, end in horizontal_segments:
        if end - start >= 2:
            fill_horizontal_line(r, start, end, 2)

    for start, end, c in vertical_segments:
        if end - start >= 2:
            fill_vertical_line(start, end, c, 2)

    return grid