def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        if all(grid[r][c] == grid[r][0] for c in range(cols)):
            break
    return [row[1:cols-1] for row in grid[r+1:rows] if not all(row[c] == row[0] for c in range(cols))]