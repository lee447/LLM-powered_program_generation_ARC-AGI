from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    colors = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 2:
                colors.add(grid[r][c])
    region_colors = sorted(colors)
    small, large = region_colors[0], region_colors[1]
    bounds = {}
    for col in region_colors:
        cmin = w; cmax = -1
        for r in range(h):
            for c in range(w):
                if grid[r][c] == col:
                    if c < cmin: cmin = c
                    if c > cmax: cmax = c
        bounds[col] = (cmin, cmax)
    new_grid = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2 and not vis[r][c]:
                stack = [(r,c)]
                cells = []
                vis[r][c] = True
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]==2 and not vis[nx][ny]:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                rs = [x for x,y in cells]; cs = [y for x,y in cells]
                rmin, cmin = min(rs), min(cs)
                height = max(rs) - rmin + 1
                width_ = max(cs) - cmin + 1
                region_col = None
                for dx,dy in ((0,-1),(0,1),(-1,0),(1,0)):
                    nr, nc = rmin+dx, cmin+dy
                    if 0<=nr<h and 0<=nc<w and grid[nr][nc] != 2:
                        region_col = grid[nr][nc]
                        break
                for x,y in cells:
                    new_grid[x][y] = region_col
                rcmin, rcmax = bounds[region_col]
                if region_col == small:
                    new_cmin = rcmax - width_ + 1
                else:
                    new_cmin = rcmin
                for x,y in cells:
                    dr = x - rmin
                    dc = y - cmin
                    new_grid[rmin + dr][new_cmin + dc] = 2
    return new_grid