def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not seen[i][j]:
                comp = []
                stack = [(i,j)]
                seen[i][j]=True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==1:
                            seen[nx][ny]=True
                            stack.append((nx,ny))
                rs = [x for x,y in comp]; cs = [y for x,y in comp]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                hh = r1-r0+1; ww = c1-c0+1
                # draw frame
                for x in range(r0-1, r1+2):
                    for y in range(c0-1, c1+2):
                        if 0<=x<h and 0<=y<w:
                            if x==r0-1 or x==r1+1 or y==c0-1 or y==c1+1:
                                if res[x][y]==4:
                                    res[x][y]=2
                # recolor comp if line or square>=3
                do = ((hh==1 and ww>1) or (ww==1 and hh>1) or (hh==ww and hh>2))
                if do:
                    for x,y in comp:
                        if x==r0 or x==r1 or y==c0 or y==c1:
                            res[x][y]=8
                        else:
                            res[x][y]=6
    return res