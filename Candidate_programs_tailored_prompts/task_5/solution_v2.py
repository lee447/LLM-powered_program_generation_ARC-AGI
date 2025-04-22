def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def find_refs(val):
        pts=[]
        for r in range(h):
            for c in range(w):
                if grid[r][c]==val:
                    pts.append((r,c))
        return pts
    refs = {c:find_refs(c) for c in set(sum(grid,[])) if c!=6}
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c]==6 and not visited[r][c]:
                # flood fill component
                comp=[]
                dq=deque([(r,c)])
                visited[r][c]=True
                while dq:
                    x,y=dq.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==6:
                            visited[nx][ny]=True
                            dq.append((nx,ny))
                rows=sorted(set(x for x,y in comp))
                # choose 3 reference colors by scanning around bbox
                minr,maxr = rows[0],rows[-1]
                cols=sorted(set(y for x,y in comp))
                minc,maxc = cols[0],cols[-1]
                # collect three neighbor colors: above, inside, below
                top_colors=[]
                if minr>0:
                    for c0 in cols:
                        v=grid[minr-1][c0]
                        if v!=6: top_colors.append(v)
                mid_colors=[]
                for c0 in cols:
                    for dr in (0,1):
                        rr=minr+dr
                        if 0<=rr<h:
                            v=grid[rr][minc-1] if minc>0 else None
                            if v!=6 and v is not None: mid_colors.append(v)
                            v=grid[rr][maxc+1] if maxc+1<w else None
                            if v!=6 and v is not None: mid_colors.append(v)
                bot_colors=[]
                if maxr+1<h:
                    for c0 in cols:
                        v=grid[maxr+1][c0]
                        if v!=6: bot_colors.append(v)
                def pick(lst,default):
                    return max(set(lst),key=lst.count) if lst else default
                a=pick(top_colors,refs.keys().__iter__().__next__())
                b=pick(mid_colors,7)
                c=pick(bot_colors,refs.keys().__iter__().__next__())
                maxsum=(maxr-minr)+(maxc-minc)
                thresh = maxsum//2
                for x,y in comp:
                    s=(x-minr)+(y-minc)
                    if s==0:
                        out[x][y]=a
                    elif s>thresh:
                        out[x][y]=c
                    else:
                        out[x][y]=b
    return out