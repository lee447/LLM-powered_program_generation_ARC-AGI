def solve(grid):
    h=len(grid);w=len(grid[0])
    visited=[[False]*w for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    components=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not visited[i][j]:
                stack=[(i,j)];visited[i][j]=True;cells=[]
                while stack:
                    r,c=stack.pop()
                    cells.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0 and not visited[nr][nc]:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                components.append(cells)
    by_size={}
    for comp in components:
        s=len(comp)
        if s>1:
            by_size.setdefault(s,[]).append(comp)
    modules=[]
    for size,comps in by_size.items():
        if len(comps)>=2:
            template=None
            for comp in comps:
                rs=[r for r,c in comp]; cs=[c for r,c in comp]
                r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                h0=r1-r0+1; w0=maxc-minc+1
                if h0*w0==size:
                    pattern={(r-r0,c-minc):grid[r][c] for r,c in comp}
                    template=(h0,w0,pattern)
                    break
            if template:
                modules.append((comps,template))
    out=[[0]*w for _ in range(h)]
    for comps,(mh,mw,pattern) in modules:
        for comp in comps:
            rs=[r for r,c in comp]; cs=[c for r,c in comp]
            r0=min(rs); c0=min(cs)
            for (dr,dc),v in pattern.items():
                out[r0+dr][c0+dc]=v
    return out