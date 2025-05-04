def solve(grid):
    h, w = len(grid), len(grid[0])
    ones = [(x, y) for y in range(h) for x in range(w) if grid[y][x] == 1]
    row_counts = {}
    for x, y in ones:
        row_counts[y] = row_counts.get(y, 0) + 1
    anchor_row = next(r for r, cnt in row_counts.items() if cnt == 1)
    anchor_col = next(x for x, y in ones if y == anchor_row)
    offsets = [(x - anchor_col, y - anchor_row) for x, y in ones]
    out = [row[:] for row in grid]
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c not in (0, 1):
                for dx, dy in offsets:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and out[ny][nx] != 1:
                        out[ny][nx] = c
    return out