from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def fill_horizontal(row, start, end):
        for i in range(start, end):
            row[i] = 3

    def fill_vertical(grid, col, start, end):
        for i in range(start, end):
            grid[i][col] = 3

    def find_horizontal_bars(grid):
        bars = []
        for r, row in enumerate(grid):
            start = None
            for c, val in enumerate(row):
                if val == 3:
                    if start is None:
                        start = c
                else:
                    if start is not None:
                        bars.append((r, start, c))
                        start = None
            if start is not None:
                bars.append((r, start, len(row)))
        return bars

    def find_vertical_bars(grid):
        bars = []
        for c in range(len(grid[0])):
            start = None
            for r in range(len(grid)):
                if grid[r][c] == 3:
                    if start is None:
                        start = r
                else:
                    if start is not None:
                        bars.append((c, start, r))
                        start = None
            if start is not None:
                bars.append((c, start, len(grid)))
        return bars

    horizontal_bars = find_horizontal_bars(grid)
    vertical_bars = find_vertical_bars(grid)

    for r, start, end in horizontal_bars:
        if end - start > 1:
            fill_horizontal(grid[r], start, end)

    for c, start, end in vertical_bars:
        if end - start > 1:
            fill_vertical(grid, c, start, end)

    return grid