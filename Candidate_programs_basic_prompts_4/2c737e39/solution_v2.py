def solve(grid):
    h = len(grid)
    w = len(grid[0])
    pivots = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 5]
    if not pivots:
        return grid
    pivots.sort()
    r1, c1 = pivots[0]
    offs = []
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != 0 and v != 5:
                offs.append((i - r1, j - c1, v))
    res = [row[:] for row in grid]
    for r, c in pivots[1:]:
        for dr, dc, v in offs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and res[nr][nc] == 0:
                res[nr][nc] = v
    return res