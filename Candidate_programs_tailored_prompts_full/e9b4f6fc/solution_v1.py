def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                comp = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                            comp.append((nx, ny))
                comps.append(comp)
    comp = max(comps, key=len)
    comp_set = set(comp)
    minr = min(r for r,c in comp)
    maxr = max(r for r,c in comp)
    minc = min(c for r,c in comp)
    maxc = max(c for r,c in comp)
    mapping = {}
    for i in range(h):
        for j in range(w-1):
            if (i,j) not in comp_set and (i,j+1) not in comp_set:
                x, y = grid[i][j], grid[i][j+1]
                if x and y:
                    mapping[y] = x
    out = []
    for i in range(minr, maxr+1):
        row = []
        for j in range(minc, maxc+1):
            v = grid[i][j]
            row.append(mapping.get(v, v) if v else 0)
        out.append(row)
    return out