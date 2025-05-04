def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    greys = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 5]
    minr = min(r for r, c in greys)
    maxr = max(r for r, c in greys)
    minc = min(c for r, c in greys)
    maxc = max(c for r, c in greys)
    key_cells = [(r, c) for r in range(minr, maxr + 1) for c in range(minc, maxc + 1) if grid[r][c] not in (0, 5)]
    r0, c0 = key_cells[0]
    key = grid[r0][c0]
    output = [[grid[r][c] for c in range(cols)] for r in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if output[r][c] == key and not (minr <= r <= maxr and minc <= c <= maxc):
                output[r][c] = 0
    return output