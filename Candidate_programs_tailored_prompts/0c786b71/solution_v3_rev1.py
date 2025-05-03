def solve(grid):
    h = len(grid)
    w = len(grid[0])
    row_tiles = [grid[i][::-1] + grid[i] for i in range(h)]
    return [row_tiles[i] for i in range(h - 1, -1, -1)] + row_tiles