from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    visited=[[False]*w for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for y in range(h):
        for x in range(w):
            if grid[y][x]!=0 and not visited[y][x]:
                col=grid[y][x]
                stack=[(y,x)]
                comp=[]
                visited[y][x]=True
                while stack:
                    cy,cx=stack.pop()
                    comp.append((cy,cx))
                    for dy,dx in dirs:
                        ny,nx=cy+dy,cx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==col:
                            visited[ny][nx]=True
                            stack.append((ny,nx))
                miny=min(p[0] for p in comp); maxy=max(p[0] for p in comp)
                minx=min(p[1] for p in comp); maxx=max(p[1] for p in comp)
                bh=maxy-miny+1; bw=maxx-minx+1
                mask=[[grid[miny+i][minx+j]==0 for j in range(bw)] for i in range(bh)]
                vis2=[[False]*bw for _ in range(bh)]
                from collections import deque
                dq=deque()
                for i in range(bh):
                    for j in (0,bw-1):
                        if mask[i][j]:
                            vis2[i][j]=True; dq.append((i,j))
                for j in range(bw):
                    for i in (0,bh-1):
                        if mask[i][j] and not vis2[i][j]:
                            vis2[i][j]=True; dq.append((i,j))
                while dq:
                    i,j=dq.popleft()
                    for di,dj in dirs:
                        ni,nj=i+di,j+dj
                        if 0<=ni<bh and 0<=nj<bw and mask[ni][nj] and not vis2[ni][nj]:
                            vis2[ni][nj]=True; dq.append((ni,nj))
                hole=False
                for i in range(bh):
                    for j in range(bw):
                        if mask[i][j] and not vis2[i][j]:
                            hole=True; break
                    if hole: break
                if hole:
                    out=[grid[miny+i][minx:maxx+1] for i in range(bh)]
                    return out
    return []