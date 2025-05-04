def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    shapes = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]==1 and not vis[r][c]:
                q = deque([(r,c)])
                vis[r][c]=True
                cells=[]
                while q:
                    x,y=q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==1:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                rs = [x for x,y in cells]
                cs = [y for x,y in cells]
                r0,c0,r1,c1 = min(rs),min(cs),max(rs),max(cs)
                ph, pw = r1-r0+1, c1-c0+1
                mask=[[0]*pw for _ in range(ph)]
                for x,y in cells:
                    mask[x-r0][y-c0]=1
                shapes.append((r0,c0,ph,pw,mask))
    shapes.sort(key=lambda t:(t[0],t[1]))
    if not shapes:
        return g
    first_r, first_c, ph, pw, mask = shapes[0]
    row0 = first_r; col0 = first_c
    col_count = sum(1 for r0,c0,_,_,_ in shapes if r0==row0)
    step_r = ph+1; step_c = pw+1
    anchors = [(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c]!=0 and grid[r][c]!=1]
    anchors.sort(key=lambda t:(t[0],t[1]))
    for i,(ar,ac,color) in enumerate(anchors):
        br = i//col_count; bc = i%col_count
        r_start = row0 + br*step_r
        c_start = col0 + bc*step_c
        if i < len(shapes):
            r0i,c0i,hi,wi,mi = shapes[i]
            for dr in range(hi):
                for dc in range(wi):
                    if mi[dr][dc]:
                        g[r0i+dr][c0i+dc] = color
        else:
            for dr in range(ph):
                for dc in range(pw):
                    if mask[dr][dc]:
                        rr,cc = r_start+dr, c_start+dc
                        if 0<=rr<h and 0<=cc<w:
                            g[rr][cc] = color
    return g