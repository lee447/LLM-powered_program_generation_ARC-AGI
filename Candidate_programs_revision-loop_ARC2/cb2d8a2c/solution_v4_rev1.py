from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    # find the unique color c
    counts = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 8:
                counts[v] = counts.get(v, 0) + 1
    c = next(col for col, cnt in counts.items() if cnt == 1)
    # collect stripe cells (non-c, non-8)
    stripe = {(r, x) for r in range(h) for x in range(w) if grid[r][x] not in (8, c)}
    # unify stripes to max color
    if stripe:
        maxcol = max(grid[r][x] for r, x in stripe)
        for r, x in stripe:
            grid[r][x] = maxcol
    # find all neighbors of the stripe's bounding box
    ys = [r for r, _ in stripe]
    xs = [x for _, x in stripe]
    if stripe:
        y0, y1 = min(ys), max(ys)
        x0, x1 = min(xs), max(xs)
    else:
        # no stripe: just return
        return grid
    # build set of candidate endpoints: background cells adjacent to the stripe rectangle
    cand = set()
    for y in (y0 - 1, y1 + 1):
        if 0 <= y < h:
            for x in range(x0, x1 + 1):
                if 0 <= x < w and grid[y][x] == 8:
                    cand.add((y, x))
    for x in (x0 - 1, x1 + 1):
        if 0 <= x < w:
            for y in range(y0, y1 + 1):
                if 0 <= y < h and grid[y][x] == 8:
                    cand.add((y, x))
    # locate c
    for r in range(h):
        for x in range(w):
            if grid[r][x] == c:
                sy, sx = r, x
                break
    # BFS to find path from (sy,sx) to any candidate without stepping on stripe
    prev = [[None] * w for _ in range(h)]
    q = deque([(sy, sx)])
    seen = { (sy, sx) }
    target = None
    while q and target is None:
        y, x = q.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and (ny, nx) not in seen:
                if grid[ny][nx] == 8 and (ny, nx) not in stripe or (ny, nx) in cand:
                    seen.add((ny, nx))
                    prev[ny][nx] = (y, x)
                    if (ny, nx) in cand:
                        target = (ny, nx)
                        break
                    q.append((ny, nx))
    # paint the path
    if target:
        y, x = target
        while (y, x) != (sy, sx):
            grid[y][x] = c
            y, x = prev[y][x]
        grid[sy][sx] = c
    return grid