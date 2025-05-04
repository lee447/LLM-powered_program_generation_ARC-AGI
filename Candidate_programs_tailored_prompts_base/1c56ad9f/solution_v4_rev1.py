def solve(grid):
    h, w = len(grid), len(grid[0])
    c = next((v for row in grid for v in row if v != 0), None)
    if c is None:
        return grid
    row_counts = [sum(1 for v in row if v == c) for row in grid]
    edges_count = max(row_counts)
    top = next(i for i, cnt in enumerate(row_counts) if cnt == edges_count)
    bottom = max(i for i, cnt in enumerate(row_counts) if cnt == edges_count)
    x0 = next(i for i, v in enumerate(grid[top]) if v == c)
    x1 = max(i for i, v in enumerate(grid[top]) if v == c)
    bars = sorted({x for y in range(top+1, bottom) for x in range(w) if grid[y][x] == c})
    shifts = [0, -1, 0, 1]
    out = [[0]*w for _ in range(h)]
    for y in range(top, bottom+1):
        k = y - top
        dx = shifts[k % 4]
        if row_counts[y] == edges_count:
            for x in range(x0, x1+1):
                nx = x + dx
                if 0 <= nx < w:
                    out[y][nx] = c
        else:
            for x in bars:
                nx = x + dx
                if 0 <= nx < w:
                    out[y][nx] = c
    return out