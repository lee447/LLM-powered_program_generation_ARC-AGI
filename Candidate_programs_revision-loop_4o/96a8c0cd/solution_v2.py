def solve(grid):
    def fill_horizontal_line(row, start_col, end_col, color):
        for col in range(start_col, end_col + 1):
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

    segments = find_horizontal_segments()
    for r, start, end in segments:
        if end - start >= 2:
            fill_horizontal_line(r, start, end, 2)

    return grid