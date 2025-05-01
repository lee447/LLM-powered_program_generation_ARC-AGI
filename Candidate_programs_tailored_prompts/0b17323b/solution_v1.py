def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    blues = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]
    if len(blues) < 2:
        return grid
    blues.sort()
    dr = blues[1][0] - blues[0][0]
    dc = blues[1][1] - blues[0][1]
    r, c = blues[-1]
    nr, nc = r + dr, c + dc
    while 0 <= nr < rows and 0 <= nc < cols:
        grid[nr][nc] = 2
        nr += dr
        nc += dc
    return grid