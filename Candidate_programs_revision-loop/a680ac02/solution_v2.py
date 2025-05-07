def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    shapes = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0 and not visited[y][x]:
                c = grid[y][x]
                stack = [(y, x)]
                comp = []
                while stack:
                    cy, cx = stack.pop()
                    if 0 <= cy < h and 0 <= cx < w and not visited[cy][cx] and grid[cy][cx] == c:
                        visited[cy][cx] = True
                        comp.append((cy, cx))
                        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                            ny, nx = cy+dy, cx+dx
                            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == c:
                                stack.append((ny, nx))
                ys = [p[0] for p in comp]
                xs = [p[1] for p in comp]
                miny, maxy = min(ys), max(ys)
                minx, maxx = min(xs), max(xs)
                if maxy-miny+1 == 4 and maxx-minx+1 == 4 and len(comp) == 12:
                    pat = [[grid[miny+dy][minx+dx] for dx in range(4)] for dy in range(4)]
                    shapes.append((miny, minx, pat))
    if not shapes:
        return []
    xs = [s[1] for s in shapes]
    ys = [s[0] for s in shapes]
    hor = (max(xs) - min(xs)) >= (max(ys) - min(ys))
    if hor:
        shapes.sort(key=lambda s: s[1])
        out = [[ ] for _ in range(4)]
        for _, _, pat in shapes:
            for i in range(4):
                out[i].extend(pat[i])
    else:
        shapes.sort(key=lambda s: s[0])
        out = []
        for _, _, pat in shapes:
            for row in pat:
                out.append(list(row))
    return out