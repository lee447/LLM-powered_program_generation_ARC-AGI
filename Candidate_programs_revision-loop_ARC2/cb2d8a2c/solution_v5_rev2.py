from collections import deque, defaultdict
def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = 8
    coords = defaultdict(list)
    for y in range(h):
        for x in range(w):
            v = grid[y][x]
            if v != bg:
                coords[v].append((y, x))
    vert = horiz = None
    for v, pts in coords.items():
        ys = [y for y, x in pts]
        xs = [x for y, x in pts]
        if min(xs) == max(xs) and max(ys) > min(ys):
            vert = v
        if min(ys) == max(ys) and max(xs) > min(xs):
            horiz = v
    c = vert
    stripe_color = horiz
    stripe = set(coords[stripe_color])
    ys = [y for y, x in stripe]
    xs = [x for y, x in stripe]
    y0, y1 = min(ys), max(ys)
    x0, x1 = min(xs), max(xs)
    pts = coords[c]
    avg_stripe_y = sum(y for y, x in stripe) / len(stripe)
    avg_c_y = sum(y for y, x in pts) / len(pts)
    if avg_stripe_y > avg_c_y:
        sy, sx = max(pts)
    else:
        sy, sx = min(pts)
    prev = [[None] * w for _ in range(h)]
    q = deque([(sy, sx)])
    seen = { (sy, sx) }
    cand = set()
    for y in (y0 - 1, y1 + 1):
        if 0 <= y < h:
            for x in range(x0, x1 + 1):
                if grid[y][x] == bg:
                    cand.add((y, x))
    for x in (x0 - 1, x1 + 1):
        if 0 <= x < w:
            for y in range(y0, y1 + 1):
                if grid[y][x] == bg:
                    cand.add((y, x))
    target = None
    while q and target is None:
        y, x = q.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and (ny, nx) not in seen:
                if grid[ny][nx] == bg and (ny, nx) not in stripe or (ny, nx) in cand:
                    seen.add((ny, nx))
                    prev[ny][nx] = (y, x)
                    if (ny, nx) in cand:
                        target = (ny, nx)
                        break
                    q.append((ny, nx))
    if target:
        y, x = target
        while (y, x) != (sy, sx):
            grid[y][x] = c
            y, x = prev[y][x]
        grid[sy][sx] = c
    return grid