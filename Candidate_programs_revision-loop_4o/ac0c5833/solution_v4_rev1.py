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

    red_segments = find_red_segments(grid)
    extend_segments(red_segments, grid)
    return grid