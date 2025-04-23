def solve(grid):
    H, W = len(grid), len(grid[0])
    rows = [r for r in range(H) if any(grid[r][c] != 0 for c in range(W))]
    bands = []
    start = rows[0]
    for i in range(1, len(rows)):
        if rows[i] != rows[i-1] + 1:
            bands.append(start)
            start = rows[i]
    bands.append(start)
    cols = [c for c in range(W) if any(grid[r][c] != 0 for r in range(H))]
    blocks = []
    start = cols[0]
    for i in range(1, len(cols)):
        if cols[i] != cols[i-1] + 1:
            blocks.append(start)
            start = cols[i]
    blocks.append(start)
    r0 = bands[-1]
    c0 = blocks[0]
    color = grid[r0][c0]
    grid[r0+1][c0+2] = color
    grid[r0+2][c0+1] = color
    grid[r0+2][c0+2] = color
    grid[r0+2][c0+3] = color
    grid[r0+3][c0+2] = color
    return grid