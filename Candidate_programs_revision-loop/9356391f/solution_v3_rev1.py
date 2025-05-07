def solve(grid):
    h, w = len(grid), len(grid[0])
    colors = [c for c in grid[0] if c != 0]
    out = [row[:] for row in grid]
    cy = cx = None
    for y in range(2, h):
        for x in range(w):
            if grid[y][x] != 0:
                cy, cx = y, x
                break
        if cy is not None:
            break
    for r, c in enumerate(colors):
        for y in range(h):
            for x in range(w):
                if max(abs(y - cy), abs(x - cx)) == r:
                    out[y][x] = c
    return out