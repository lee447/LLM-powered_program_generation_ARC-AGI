from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    comp_id = [[-1]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and comp_id[i][j]<0:
                q=deque([(i,j)])
                cid=len(comps)
                comp_id[i][j]=cid
                pts=[(i,j)]
                while q:
                    x,y=q.popleft()
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]==1 and comp_id[nx][ny]<0:
                            comp_id[nx][ny]=cid
                            q.append((nx,ny))
                            pts.append((nx,ny))
                comps.append(pts)
    largest = max(range(len(comps)), key=lambda k: len(comps[k])) if comps else -1
    colors = [2,8,6]
    out = [row[:] for row in grid]
    if largest>=0:
        for x,y in comps[largest]:
            out[x][y]=4
    for cid, pts in enumerate(comps):
        layers = 3 if cid==largest else 1
        shell = set(pts)
        for d in range(layers):
            nxt = set()
            for x,y in shell:
                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<h and 0<=ny<w and out[nx][ny]==4:
                        nxt.add((nx,ny))
            for x,y in nxt:
                out[x][y] = colors[d]
            shell |= nxt
    return out