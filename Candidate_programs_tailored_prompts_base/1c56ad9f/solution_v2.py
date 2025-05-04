def solve(grid):
    h, w = len(grid), len(grid[0])
    c = next((grid[y][x] for y in range(h) for x in range(w) if grid[y][x] != 0), None)
    if c is None:
        return grid
    row_counts = [sum(1 for v in row if v == c) for row in grid]
    edges_count = max(row_counts)
    inner_counts = [cnt for cnt in row_counts if 0 < cnt < edges_count]
    bars_count = min(inner_counts) if inner_counts else 0
    top = next(y for y, cnt in enumerate(row_counts) if cnt == edges_count)
    bottom = (h - 1) - next(i for i, cnt in enumerate(reversed(row_counts)) if cnt == edges_count)
    x0 = next(x for x in range(w) if grid[top][x] == c)
    x1 = w - 1 - next(i for i, v in enumerate(reversed(grid[top])) if v == c)
    bars = sorted({x for y in range(top+1, bottom) for x in range(w) if grid[y][x] == c})
    out = [[0]*w for _ in range(h)]
    shift_map = {0:0,1:-1,2:0,3:1}
    for y in range(h):
        if top <= y <= bottom:
            k = y - top
            dx = shift_map[k % 4]
            if k == 0 or k == bottom - top:
                nx0, nx1 = x0 + dx, x1 + dx
                for x in range(nx0, nx1+1):
                    if 0 <= x < w:
                        out[y][x] = c
            for bx in bars:
                x = bx + dx
                if 0 <= x < w and y not in (top, bottom):
                    out[y][x] = c
    return out