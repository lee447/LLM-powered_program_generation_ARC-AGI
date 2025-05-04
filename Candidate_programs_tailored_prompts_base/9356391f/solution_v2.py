def solve(grid):
    h, w = len(grid), len(grid[0])
    prefix = []
    for x in range(w):
        if grid[0][x] == 0:
            break
        prefix.append(grid[0][x])
    dot = None
    for x in range(len(prefix), w):
        if grid[0][x] != 0:
            dot = grid[0][x]
            break
    if dot is not None:
        outer = dot
        inner = list(reversed(prefix))
    else:
        outer = prefix[-1]
        inner = list(reversed(prefix[:-1]))
    frames = [outer] + inner[:2]
    ar = ac = None
    center = None
    for r in range(2, h):
        for c in range(w):
            if grid[r][c] != 0:
                ar, ac = r, c
                center = grid[r][c]
                break
        if ar is not None:
            break
    out = [row[:] for row in grid]
    layers = len(frames)
    for i, col in enumerate(frames):
        off = layers - i
        r0, r1 = ar - off, ar + off
        c0, c1 = ac - off, ac + off
        if 0 <= r0 < h:
            for x in range(c0, c1 + 1):
                if 0 <= x < w:
                    out[r0][x] = col
        if 0 <= r1 < h:
            for x in range(c0, c1 + 1):
                if 0 <= x < w:
                    out[r1][x] = col
        for y in range(r0, r1 + 1):
            if 0 <= y < h:
                if 0 <= c0 < w:
                    out[y][c0] = col
                if 0 <= c1 < w:
                    out[y][c1] = col
    out[ar][ac] = center
    return out