def solve(grid):
    h,len0=len(grid),len(grid[0])
    out=[row[:] for row in grid]
    bg=1
    template=[(0,2),(0,3),(1,0),(1,1),(2,2)]
    th=len(template)
    visited=[[False]*len0 for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(len0):
            if not visited[i][j] and grid[i][j]!=bg:
                col=grid[i][j]
                stk=[(i,j)]
                comp=[]
                visited[i][j]=True
                while stk:
                    r,c=stk.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<len0 and not visited[nr][nc] and grid[nr][nc]==col:
                            visited[nr][nc]=True
                            stk.append((nr,nc))
                if len(comp)<th:
                    delta=None
                    for tr,tc in template:
                        dr=comp[0][0]-tr; dc=comp[0][1]-tc
                        ok=True
                        for r,c in comp:
                            rr=r-dr; cc=c-dc
                            if (rr,cc) not in template:
                                ok=False; break
                        if ok:
                            delta=(dr,dc)
                            break
                    if delta:
                        dr,dc=delta
                        for tr,tc in template:
                            rr,cc=tr+dr,tc+dc
                            if 0<=rr<h and 0<=cc<len0:
                                out[rr][cc]=col
    return out