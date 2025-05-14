def solve(grid):
    def find_red_segments(grid):
        segments = []
        for r in range(len(grid)):
            start = None
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    if start is None:
                        start = c
                else:
                    if start is not None:
                        segments.append((r, start, c - 1))
                        start = None
            if start is not None:
                segments.append((r, start, len(grid[0]) - 1))
        return segments

    def extend_segments(segments, grid):
        for r, start, end in segments:
            if start > 0 and grid[r][start-1] == 0:
                grid[r][start-1] = 2
            if end < len(grid[0]) - 1 and grid[r][end+1] == 0:
                grid[r][end+1] = 2

    def find_yellow_segments(grid):
        segments = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 4:
                    segments.append((r, c))
        return segments

    def extend_yellow_segments(segments, grid):
        for r, c in segments:
            if r > 0 and grid[r-1][c] == 0:
                grid[r-1][c] = 2
            if r < len(grid) - 1 and grid[r+1][c] == 0:
                grid[r+1][c] = 2
            if c > 0 and grid[r][c-1] == 0:
                grid[r][c-1] = 2
            if c < len(grid[0]) - 1 and grid[r][c+1] == 0:
                grid[r][c+1] = 2

    red_segments = find_red_segments(grid)
    extend_segments(red_segments, grid)
    yellow_segments = find_yellow_segments(grid)
    extend_yellow_segments(yellow_segments, grid)
    return grid