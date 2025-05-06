def solve(grid):
    h=len(grid);w=len(grid[0])
    positions={}
    counts={}
    for i in range(h):
        for j in range(w):
            v=grid[i][j]
            if v!=0:
                counts[v]=counts.get(v,0)+1
                positions.setdefault(v,[]).append((i,j))
    def nbrs(cell):
        r,c=cell;cnt=0
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0:
                cnt+=1
        return cnt
    marker_color=None
    for v,cnt in counts.items():
        if cnt==2:
            p1,p2=positions[v]
            n1,n2=nbrs(p1),nbrs(p2)
            if (n1>0 and n2==0) or (n2>0 and n1==0):
                marker_color=v
                break
    p1,p2=positions[marker_color]
    if nbrs(p1)>0:
        anchor,marker=p1,p2
    else:
        anchor,marker=p2,p1
    ar,ac=anchor;mr,mc=marker
    comp=[]
    seen={anchor}
    stack=[anchor]
    while stack:
        r,c=stack.pop()
        comp.append((r,c))
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc=r+dr,c+dc
            if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0 and (nr,nc) not in seen:
                seen.add((nr,nc));stack.append((nr,nc))
    dr,dc=mr-ar,mc-ac
    out=[row[:] for row in grid]
    out[mr][mc]=0
    for r,c in comp:
        if (r,c)==anchor:continue
        nr, nc = r+dr, c+dc
        if 0<=nr<h and 0<=nc<w:
            out[nr][nc]=grid[r][c]
    return out