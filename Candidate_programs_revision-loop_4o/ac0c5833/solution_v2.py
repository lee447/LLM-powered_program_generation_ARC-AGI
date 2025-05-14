def solve(grid):
    def find_red_segments(grid):
        segments = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    if c == 0 or grid[r][c-1] != 2:
                        start = c
                    if c == len(grid[0]) - 1 or grid[r][c+1] != 2:
                        end = c
                        segments.append((r, start, end))
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