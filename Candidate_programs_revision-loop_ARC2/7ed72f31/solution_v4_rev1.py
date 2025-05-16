from collections import deque

def solve(grid):
    H, W = len(grid), len(grid[0])
    bg = grid[0][0]
    dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
    dirs8 = [(dr,dc) for dr in (-1,0,1) for dc in (-1,0,1) if (dr,dc)!=(0,0)]
    visited = [[False]*W for _ in range(H)]
    red_comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]==2 and not visited[i][j]:
                comp=[]
                q=[(i,j)]
                visited[i][j]=True
                for x,y in q:
                    comp.append((x,y))
                    for dx,dy in dirs4:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==2:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                red_comps.append(comp)
    def bfs4(sr,sc,val):
        q=deque([(sr,sc)])
        seen={(sr,sc)}
        while q:
            x,y=q.popleft()
            for dx,dy in dirs4:
                nx,ny=x+dx,y+dy
                if 0<=nx<H and 0<=ny<W and (nx,ny) not in seen and grid[nx][ny]==val:
                    seen.add((nx,ny))
                    q.append((nx,ny))
        return seen
    out=[row[:] for row in grid]
    for comp in red_comps:
        rows={r for r,c in comp}
        cols={c for r,c in comp}
        if len(comp)==1:
            r0,c0=comp[0]
            seen_shapes=set()
            for dr,dc in dirs8:
                r1,c1=r0+dr,c0+dc
                if 0<=r1<H and 0<=c1<W:
                    val=grid[r1][c1]
                    if val not in (bg,2) and (r1,c1) not in seen_shapes:
                        shape=bfs4(r1,c1,val)
                        seen_shapes|=shape
                        for r,c in shape:
                            rr,cc=2*r0-r,2*c0-c
                            if 0<=rr<H and 0<=cc<W and out[rr][cc]==bg:
                                out[rr][cc]=val
        elif len(rows)==1:
            r0=next(iter(rows))
            if r0>0 and any(grid[r0-1][c] not in (bg,2) for c in range(W)):
                dr=-1
            else:
                dr=1
            seen_shapes=set()
            for c in range(W):
                r1=r0+dr
                if 0<=r1<H:
                    val=grid[r1][c]
                    if val not in (bg,2) and (r1,c) not in seen_shapes:
                        shape=bfs4(r1,c,val)
                        seen_shapes|=shape
                        for r,c0_ in shape:
                            if (dr==-1 and r< r0) or (dr==1 and r>r0):
                                rr,cc=2*r0-r,c0_
                                if 0<=rr<H and 0<=cc<W and out[rr][cc]==bg:
                                    out[rr][cc]=val
        elif len(cols)==1:
            c0=next(iter(cols))
            if c0>0 and any(grid[r][c0-1] not in (bg,2) for r in range(H)):
                dc=-1
            else:
                dc=1
            seen_shapes=set()
            for r in range(H):
                c1=c0+dc
                if 0<=c1<W:
                    val=grid[r][c1]
                    if val not in (bg,2) and (r,c1) not in seen_shapes:
                        shape=bfs4(r,c1,val)
                        seen_shapes|=shape
                        for r0_,c in shape:
                            if (dc==-1 and c< c0) or (dc==1 and c>c0):
                                rr,cc=r0_,2*c0-c
                                if 0<=rr<H and 0<=cc<W and out[rr][cc]==bg:
                                    out[rr][cc]=val
    return out