def solve(grid):
    from collections import deque
    h,len0=len(grid),len(grid[0])
    visited=[[False]*len0 for _ in range(h)]
    rects=[]
    for i in range(h):
        for j in range(len0):
            if grid[i][j]==1 and not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=True
                cells=[(i,j)]
                while q:
                    x,y=q.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<len0 and not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                rs=[r for r,c in cells]; cs=[c for r,c in cells]
                rects.append((min(rs),max(rs),min(cs),max(cs)))
    out=[row[:] for row in grid]
    for r0,r1,c0,c1 in rects:
        interior=[(r,c) for r in range(r0+1,r1) for c in range(c0+1,c1)]
        anchors=[(r,c) for r,c in interior if grid[r][c]!=0 and grid[r][c]!=1]
        if not anchors: continue
        ar,ac=anchors[0]
        acol=grid[ar][ac]
        total=len(interior)
        s=int(total**0.5)
        k=s*s
        interior.sort(key=lambda p:(abs(p[0]-ar)+abs(p[1]-ac),p[0],p[1]))
        for idx,(r,c) in enumerate(interior):
            out[r][c]=acol if idx<k else 3
    return out
def solve(grid):
    from collections import deque
    h,len0=len(grid),len(grid[0])
    visited=[[False]*len0 for _ in range(h)]
    rects=[]
    for i in range(h):
        for j in range(len0):
            if grid[i][j]==1 and not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=True
                cells=[(i,j)]
                while q:
                    x,y=q.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<len0 and not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                rs=[r for r,c in cells]; cs=[c for r,c in cells]
                rects.append((min(rs),max(rs),min(cs),max(cs)))
    out=[row[:] for row in grid]
    for r0,r1,c0,c1 in rects:
        interior=[(r,c) for r in range(r0+1,r1) for c in range(c0+1,c1)]
        anchors=[(r,c) for r,c in interior if grid[r][c]!=0 and grid[r][c]!=1]
        if not anchors: continue
        ar,ac=anchors[0]
        acol=grid[ar][ac]
        total=len(interior)
        s=int(total**0.5)
        k=s*s
        interior.sort(key=lambda p:(abs(p[0]-ar)+abs(p[1]-ac),p[0],p[1]))
        for idx,(r,c) in enumerate(interior):
            out[r][c]=acol if idx<k else 3
    return out
def solve(grid):
    from collections import deque
    h,len0=len(grid),len(grid[0])
    visited=[[False]*len0 for _ in range(h)]
    rects=[]
    for i in range(h):
        for j in range(len0):
            if grid[i][j]==1 and not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=True
                cells=[(i,j)]
                while q:
                    x,y=q.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<len0 and not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                rs=[r for r,c in cells]; cs=[c for r,c in cells]
                rects.append((min(rs),max(rs),min(cs),max(cs)))
    out=[row[:] for row in grid]
    for r0,r1,c0,c1 in rects:
        interior=[(r,c) for r in range(r0+1,r1) for c in range(c0+1,c1)]
        anchors=[(r,c) for r,c in interior if grid[r][c]!=0 and grid[r][c]!=1]
        if not anchors: continue
        ar,ac=anchors[0]
        acol=grid[ar][ac]
        total=len(interior)
        s=int(total**0.5)
        k=s*s
        interior.sort(key=lambda p:(abs(p[0]-ar)+abs(p[1]-ac),p[0],p[1]))
        for idx,(r,c) in enumerate(interior):
            out[r][c]=acol if idx<k else 3
    return out
def solve(grid):
    from collections import deque
    h,len0=len(grid),len(grid[0])
    visited=[[False]*len0 for _ in range(h)]
    rects=[]
    for i in range(h):
        for j in range(len0):
            if grid[i][j]==1 and not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=True
                cells=[(i,j)]
                while q:
                    x,y=q.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<len0 and not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                rs=[r for r,c in cells]; cs=[c for r,c in cells]
                rects.append((min(rs),max(rs),min(cs),max(cs)))
    out=[row[:] for row in grid]
    for r0,r1,c0,c1 in rects:
        interior=[(r,c) for r in range(r0+1,r1) for c in range(c0+1,c1)]
        anchors=[(r,c) for r,c in interior if grid[r][c]!=0 and grid[r][c]!=1]
        if not anchors: continue
        ar,ac=anchors[0]
        acol=grid[ar][ac]
        total=len(interior)
        s=int(total**0.5)
        k=s*s
        interior.sort(key=lambda p:(abs(p[0]-ar)+abs(p[1]-ac),p[0],p[1]))
        for idx,(r,c) in enumerate(interior):
            out[r][c]=acol if idx<k else 3
    return out
def solve(grid):
    from collections import deque
    h,len0=len(grid),len(grid[0])
    visited=[[False]*len0 for _ in range(h)]
    rects=[]
    for i in range(h):
        for j in range(len0):
            if grid[i][j]==1 and not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=True
                cells=[(i,j)]
                while q:
                    x,y=q.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<len0 and not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                rs=[r for r,c in cells]; cs=[c for r,c in cells]
                rects.append((min(rs),max(rs),min(cs),max(cs)))
    out=[row[:] for row in grid]
    for r0,r1,c0,c1 in rects:
        interior=[(r,c) for r in range(r0+1,r1) for c in range(c0+1,c1)]
        anchors=[(r,c) for r,c in interior if grid[r][c]!=0 and grid[r][c]!=1]
        if not anchors: continue
        ar,ac=anchors[0]
        acol=grid[ar][ac]
        total=len(interior)
        s=int(total**0.5)
        k=s*s
        interior.sort(key=lambda p:(abs(p[0]-ar)+abs(p[1]-ac),p[0],p[1]))
        for idx,(r,c) in enumerate(interior):
            out[r][c]=acol if idx<k else 3
    return out
def solve(grid):
    from collections import deque
    h,len0=len(grid),len(grid[0])
    visited=[[False]*len0 for _ in range(h)]
    rects=[]
    for i in range(h):
        for j in range(len0):
            if grid[i][j]==1 and not visited[i][j]:
                q=deque([(i,j)])
                visited[i][j]=True
                cells=[(i,j)]
                while q:
                    x,y=q.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<len0 and not visited[nx][ny] and grid[nx][ny]==1:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                rs=[r for r,c in cells]; cs=[c for r,c in cells]
                rects.append((min(rs),max(rs),min(cs),max(cs)))
    out=[row[:] for row in grid]
    for r0,r1,c0,c1 in rects:
        interior=[(r,c) for r in range(r0+1,r1) for c in range(c0+1,c1)]
        anchors=[(r,c) for r,c in interior if grid[r][c]!=0 and grid[r][c]!=1]
        if not anchors: continue
        ar,ac=anchors[0]
        acol=grid[ar][ac]
        total=len(interior)
        s=int(total**0.5)
        k=s*s
        interior.sort(key=lambda p:(abs(p[0]-ar)+abs(p[1]-ac),p[0],p[1]))
        for idx,(r,c) in enumerate(interior):
            out[r][c]=acol if idx<k else 3
    return out
def solve(grid):
    from collections import deque
    h,w=len(grid),len(grid[0])
    vis=[[False]*w for _ in range(h)]
    rects=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not vis[i][j]:
                q=deque([(i,j)])
                vis[i][j]=True
                comp=[(i,j)]
                while q:
                    x,y=q.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==1:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                rs=[r for r,c in comp]; cs=[c for r,c in comp]
                rects.append((min(rs),max(rs),min(cs),max(cs)))
    out=[row[:] for row in grid]
    for r0,r1,c0,c1 in rects:
        interior=[(r,c) for r in range(r0+1,r1) for c in range(c0+1,c1)]
        anchors=[(r,c) for r,c in interior if grid[r][c]>1]
        if not anchors: continue
        ar,ac=anchors[0]
        acol=grid[ar][ac]
        n=len(interior)
        s=int(n**0.5)
        k=s*s
        interior.sort(key=lambda p:(abs(p[0]-ar)+abs(p[1]-ac),p[0],p[1]))
        for idx,(r,c) in enumerate(interior):
            out[r][c]=acol if idx<k else 3
    return out