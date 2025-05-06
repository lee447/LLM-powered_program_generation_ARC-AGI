def solve(grid):
    h, w = len(grid), len(grid[0])
    reds = [(y, x) for y in range(h) for x in range(w) if grid[y][x] == 2]
    visited = set()
    comps = []
    for r in reds:
        if r in visited:
            continue
        stack = [r]
        comp = []
        while stack:
            y, x = stack.pop()
            if (y, x) in visited:
                continue
            visited.add((y, x))
            comp.append((y, x))
            for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 2 and (ny, nx) not in visited:
                    stack.append((ny, nx))
        comps.append(comp)
    yellows = [(y, x) for y in range(h) for x in range(w) if grid[y][x] == 4]
    best = None
    for comp in comps:
        for cy, cx in yellows:
            d = min(abs(ry-cy)+abs(rx-cx) for ry, rx in comp)
            if best is None or d < best[0]:
                best = (d, comp, (cy, cx))
    _, seed_comp, (sy, sx) = best
    offsets = [(ry-sy, rx-sx) for ry, rx in seed_comp]
    out = [row[:] for row in grid]
    for cy, cx in yellows:
        for dy, dx in offsets:
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < h and 0 <= nx < w and out[ny][nx] == 0:
                out[ny][nx] = 2
    return out