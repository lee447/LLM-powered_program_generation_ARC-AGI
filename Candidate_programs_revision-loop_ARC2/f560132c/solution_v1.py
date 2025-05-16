def solve(grid):
    from collections import deque
    R,L=len(grid),len(grid[0])
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    def neigh(r,c):
        for dr,dc in dirs:
            rr,cc=r+dr,c+dc
            if 0<=rr<R and 0<=cc<L:
                yield rr,cc
    # find interior 2x2 block with 4 distinct non-zero colors
    inter=None
    for i in range(R-1):
        for j in range(L-1):
            s={grid[i][j],grid[i][j+1],grid[i+1][j],grid[i+1][j+1]}
            if 0 in s: s.remove(0)
            if len(s)==4:
                inter=[(i,j)]
                vals=[grid[i][j],grid[i][j+1],grid[i+1][j],grid[i+1][j+1]]
                inter_cells=[(i,j,grid[i][j]),(i,j+1,grid[i][j+1]),(i+1,j,grid[i+1][j]),(i+1,j+1,grid[i+1][j+1])]
                break
        if inter: break
    # border color is the one adjacent to those interior cells
    border_color=None
    for r,c,_ in inter_cells:
        for rr,cc in neigh(r,c):
            v=grid[rr][cc]
            if v!=0 and v not in [x[2] for x in inter_cells]:
                border_color=v
                break
        if border_color is not None:
            break
    # flood fill border component
    seen=set()
    B=[]
    dq=deque()
    dq.append((inter_cells[0][0]-1,inter_cells[0][1]))
    # find a starting border cell by scanning neighbors
    for r,c,_ in inter_cells:
        for rr,cc in neigh(r,c):
            if grid[rr][cc]==border_color:
                dq.clear()
                dq.append((rr,cc))
                break
        if dq:
            break
    while dq:
        r,c=dq.popleft()
        if (r,c) in seen: continue
        if grid[r][c]!=border_color: continue
        seen.add((r,c))
        B.append((r,c))
        for rr,cc in neigh(r,c):
            if (rr,cc) not in seen and grid[rr][cc]==border_color:
                dq.append((rr,cc))
    # origin at top-left of interior block
    oi,oj=inter_cells[0][0],inter_cells[0][1]
    offs=[(r-oi,c-oj,val) for r,c,val in inter_cells]
    # dilate
    outmap={}
    for br,bc in B:
        for dr,dc,val in offs:
            rr,cc=br-oi+dr,bc-oj+dc
            outmap[(rr,cc)]=val
    minr=min(r for r,c in outmap)
    minc=min(c for r,c in outmap)
    maxr=max(r for r,c in outmap)
    maxc=max(c for r,c in outmap)
    H,W=maxr-minr+1,maxc-minc+1
    out=[[0]*W for _ in range(H)]
    for (r,c),v in outmap.items():
        out[r-minr][c-minc]=v
    return out