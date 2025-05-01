def solve(grid):
    rows, cols = len(grid), len(grid[0])
    coords = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 8]
    r0, r1 = min(r for r, c in coords), max(r for r, c in coords)
    c0, c1 = min(c for r, c in coords), max(c for r, c in coords)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    return [row[c0 - W:c0] for row in grid[r0 - H:r0]]