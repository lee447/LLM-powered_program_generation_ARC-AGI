def solve(grid):
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if orig[i][j]==1 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                coords = []
                rmin=rmax=i; cmin=cmax=j
                for x,y in stack:
                    coords.append((x,y))
                    if x<rmin: rmin=x
                    if x>rmax: rmax=x
                    if y<cmin: cmin=y
                    if y>cmax: cmax=y
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and orig[nx][ny]==1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                comps.append((coords, rmin, rmax, cmin, cmax))
    for coords, rmin, rmax, cmin, cmax in comps:
        for j in range(cmin-1, cmax+2):
            for i in (rmin-1, rmax+1):
                if 0<=i<h and 0<=j<w and res[i][j]==4:
                    res[i][j] = 2
        for i in range(rmin-1, rmax+2):
            for j in (cmin-1, cmax+1):
                if 0<=i<h and 0<=j<w and res[i][j]==4:
                    res[i][j] = 2
        for i in range(rmin, rmax+1):
            for j in range(cmin, cmax+1):
                if res[i][j]==4:
                    res[i][j] = 8
    squares = [c for c in comps if c[2]-c[1] == c[4]-c[3] and c[2]-c[1]>0]
    squares.sort(key=lambda c: c[3])
    for sq in squares[1:]:
        for i,j in sq[0]:
            res[i][j] = 6
    return res