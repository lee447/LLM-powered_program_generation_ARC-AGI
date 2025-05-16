def solve(grid):
    rows, cols = len(grid), len(grid[0])
    sep = [c for c in range(cols) if all(grid[r][c] == grid[0][c] for r in range(rows))]
    c0, c1 = sep[0], sep[1]
    return [row[c0:c1+1] for row in grid]