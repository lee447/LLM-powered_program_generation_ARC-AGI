def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                for rr in range(r, rows):
                    grid[rr][c] = grid[r][c]
    return grid