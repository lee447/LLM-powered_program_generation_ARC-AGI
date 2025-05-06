from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    grey = 5
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    vis = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==grey and not vis[i][j]:
                stack = [(i,j)]
                comp = []
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==grey:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                rs = [x for x,_ in comp]
                cs = [y for _,y in comp]
                rmin,rmax,cmin,cmax = min(rs),max(rs),min(cs),max(cs)
                # fill hole interior
                for x in range(rmin+1,rmax):
                    for y in range(cmin+1,cmax):
                        if grid[x][y]==0:
                            grid[x][y] = 2
                # find broken border
                broken = []
                for y in range(cmin+1,cmax):
                    for x in (rmin,rmax):
                        if grid[x][y]==0 and y-1>=0 and y+1<w and grid[x][y-1]==grey and grid[x][y+1]==grey:
                            grid[x][y] = 2
                            broken.append((x,y))
                for x,y in broken:
                    # find interior neighbor and outward
                    if x+1<h and grid[x+1][y]==2:
                        ix,iy = x+1,y
                        ox,oy = x-1,y
                    else:
                        ix,iy = x-1,y
                        ox,oy = x+1,y
                    # choose horizontal dir by interior shape
                    if iy-1>=0 and grid[ix][iy-1]==2:
                        dh = -1
                    else:
                        dh = 1
                    # extend path
                    if 0<=ox<h and 0<=oy<w and grid[ox][oy]==0:
                        grid[ox][oy] = 2
                        cy = oy
                        while True:
                            cy += dh
                            if 0<=cy<w and grid[ox][cy]==0:
                                grid[ox][cy] = 2
                            else:
                                break
    return grid