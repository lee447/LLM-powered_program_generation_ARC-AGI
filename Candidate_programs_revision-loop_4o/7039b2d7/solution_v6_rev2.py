def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    start_row = 0
    end_row = rows
    for r in range(rows):
        if all(grid[r][c] == grid[r][0] for c in range(cols)):
            start_row = r + 1
            break
    for r in range(rows-1, -1, -1):
        if all(grid[r][c] == grid[r][0] for c in range(cols)):
            end_row = r
            break
    return [row[1:cols-1] for row in grid[start_row:end_row] if not all(row[c] == row[0] for c in range(cols))]