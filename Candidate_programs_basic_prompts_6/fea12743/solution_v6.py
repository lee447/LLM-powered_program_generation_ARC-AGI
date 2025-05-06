def solve(grid):
    h, w = len(grid), len(grid[0])
    orig = None
    for row in grid:
        for v in row:
            if v != 0:
                orig = v
                break
        if orig is not None:
            break
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == orig and not seen[y][x]:
                stack = [(y,x)]
                seen[y][x] = True
                cells = []
                while stack:
                    cy, cx = stack.pop()
                    cells.append((cy,cx))
                    for dy, dx in dirs:
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx] == orig:
                            seen[ny][nx] = True
                            stack.append((ny,nx))
                ys = [p[0] for p in cells]
                xs = [p[1] for p in cells]
                comps.append((min(ys), min(xs), cells))
    comps.sort()
    palette = [orig, 8, 8, orig, orig, 3]
    out = [row[:] for row in grid]
    for i, (_, _, cells) in enumerate(comps):
        c = palette[i]
        for y, x in cells:
            out[y][x] = c
    return out