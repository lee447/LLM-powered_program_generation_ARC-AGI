def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [row[:] for row in grid]
    rows_with_5 = [r for r in range(h) for c in range(w) if grid[r][c] == 5]
    if rows_with_5:
        anchor_bottom = max(rows_with_5)
        for r in range(anchor_bottom + 1, h):
            if (r - anchor_bottom) % 4 == 1:
                cols = [c for c in range(w) if grid[r][c] != 0 and grid[r][c] != 5]
                if cols:
                    out[r][max(cols)] = 0
    return out