def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    visited = [[False]*w for _ in range(h)]
    shapes = set()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                comp = []
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 5:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                forms = []
                for fx in (1, -1):
                    for fy in (1, -1):
                        for swap in (False, True):
                            pts = []
                            for x, y in comp:
                                tx, ty = (y, x) if swap else (x, y)
                                pts.append((tx*fx, ty*fy))
                            minx = min(x for x, y in pts)
                            miny = min(y for x, y in pts)
                            norm = tuple(sorted((x-minx, y-miny) for x, y in pts))
                            forms.append(norm)
                shapes.add(min(forms))
    cnt = len(shapes)
    return [[0] for _ in range(cnt)]