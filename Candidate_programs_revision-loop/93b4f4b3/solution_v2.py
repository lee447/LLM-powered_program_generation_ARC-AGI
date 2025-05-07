def solve(grid):
    h = len(grid)
    w = len(grid[0])
    mid = w // 2
    visited_hole = [[False] * mid for _ in range(h)]
    holes = []
    for i in range(h):
        for j in range(mid):
            if grid[i][j] == 0 and not visited_hole[i][j]:
                stack = [(i, j)]
                visited_hole[i][j] = True
                coords = []
                while stack:
                    x, y = stack.pop()
                    coords.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < mid and not visited_hole[nx][ny] and grid[nx][ny] == 0:
                            visited_hole[nx][ny] = True
                            stack.append((nx, ny))
                minr = min(x for x, y in coords)
                minc = min(y for x, y in coords)
                maxr = max(x for x, y in coords)
                maxc = max(y for x, y in coords)
                mask = {(x - minr, y - minc) for x, y in coords}
                holes.append((minr, minc, maxr-minr+1, maxc-minc+1, mask, coords))
    visited_shape = [[False] * w for _ in range(h)]
    shapes = {}
    for i in range(h):
        for j in range(mid, w):
            if grid[i][j] != 0 and not visited_shape[i][j]:
                color = grid[i][j]
                stack = [(i, j)]
                visited_shape[i][j] = True
                coords = []
                while stack:
                    x, y = stack.pop()
                    coords.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and mid <= ny < w and not visited_shape[nx][ny] and grid[nx][ny] == color:
                            visited_shape[nx][ny] = True
                            stack.append((nx, ny))
                minr = min(x for x, y in coords)
                minc = min(y for x, y in coords)
                maxr = max(x for x, y in coords)
                maxc = max(y for x, y in coords)
                mask = {(x - minr, y - minc) for x, y in coords}
                key = (maxr-minr+1, maxc-minc+1, tuple(sorted(mask)))
                shapes[key] = color
    out = [row[:mid] for row in grid]
    for minr, minc, hh, ww, mask, coords in holes:
        key = (hh, ww, tuple(sorted(mask)))
        if key in shapes:
            c = shapes[key]
            for x, y in coords:
                out[x][y] = c
    return out