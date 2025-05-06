def solve(grid):
    h=len(grid); w=len(grid[0])
    orig=[row[:] for row in grid]
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if orig[i][j]!=0 and not visited[i][j]:
                stack=[(i,j)]; comp=[]
                visited[i][j]=True
                while stack:
                    r,c=stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and orig[nr][nc]!=0:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                comps.append(comp)
    for comp in comps:
        rs=[r for r,_ in comp]; cs=[c for _,c in comp]
        r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
        height=r1-r0+1; width=c1-c0+1
        pattern_rows=[r for r in range(r0,r1+1) if all(orig[r][c]!=0 for c in range(c0,c1+1))]
        pattern_cols=[c for c in range(c0,c1+1) if all(orig[r][c]!=0 for r in range(r0,r1+1))]
        if len(pattern_rows)>1 and len(pattern_cols)==1:
            mode='h'
        elif len(pattern_cols)>1 and len(pattern_rows)==1:
            mode='v'
        else:
            if height>width:
                mode='v'
            else:
                mode='h'
        for r in range(r0,r1+1):
            for c in range(c0,c1+1):
                if orig[r][c]==0:
                    if mode=='h':
                        pr=pattern_rows[(r-r0)%len(pattern_rows)]
                        grid[r][c]=orig[pr][c]
                    else:
                        pc=pattern_cols[(c-c0)%len(pattern_cols)]
                        grid[r][c]=orig[r][pc]
    return grid