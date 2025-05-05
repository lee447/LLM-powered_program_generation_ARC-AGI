def solve(grid):
    mapping = {8: 2, 3: 1, 5: 4}
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    anchor = next((v for row in grid for v in row if v != 0), 0)
    fill = mapping.get(anchor, 0)
    return [[0 if grid[i][j] != 0 else fill for j in range(cols)] for i in range(rows)]