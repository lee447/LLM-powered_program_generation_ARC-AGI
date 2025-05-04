def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                rmin = rmax = i
                cmin = cmax = j
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    if x<rmin: rmin=x
                    if x>rmax: rmax=x
                    if y<cmin: cmin=y
                    if y>cmax: cmax=y
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==8:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                for r in range(rmin, rmax+1):
                    for c in range(cmin, cmax+1):
                        if grid[r][c]==0:
                            grid[r][c]=2
    return grid