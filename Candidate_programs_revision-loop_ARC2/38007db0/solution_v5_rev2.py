def solve(grid):
    rows, cols = len(grid), len(grid[0])
    sep = [c for c in range(cols) if len({grid[r][c] for r in range(rows)}) == 1]
    c0, c1 = sep[-2], sep[-1]
    return [row[c0:c1+1] for row in grid]