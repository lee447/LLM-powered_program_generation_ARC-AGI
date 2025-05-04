from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    bg=grid[0][0]
    sep_rows=[r for r in range(h) if len(set(grid[r]))==1 and grid[r][0]!=bg]
    sep_cols=[c for c in range(w) if len({grid[r][c] for r in range(h)})==1 and grid[0][c]!=bg]
    sep_rows.sort(); sep_cols.sort()
    hranges=[]; start=0
    for r in sep_rows:
        if start<=r-1: hranges.append((start,r-1))
        start=r+1
    if start<=h-1: hranges.append((start,h-1))
    vranges=[]; start=0
    for c in sep_cols:
        if start<=c-1: vranges.append((start,c-1))
        start=c+1
    if start<=w-1: vranges.append((start,w-1))
    bcol=grid[sep_rows[0]][0] if sep_rows else (grid[0][sep_cols[0]] if sep_cols else None)
    orig=grid
    out=[row[:] for row in grid]
    block_shapes={}
    for i,(rs,re) in enumerate(hranges):
        for j,(cs,ce) in enumerate(vranges):
            cells=[]
            for r in range(rs,re+1):
                for c in range(cs,ce+1):
                    v=orig[r][c]
                    if v!=bg and v!=bcol:
                        cells.append((r,c,v))
            block_shapes[(i,j)]=cells
    for (i,j),cells in list(block_shapes.items()):
        if cells and (i,j+1) in block_shapes and not block_shapes[(i,j+1)]:
            cs,ce=vranges[j]; rs,re=hranges[i]
            for r,c,v in cells:
                nc=cs+(ce-c)
                out[r][nc]=v
    return out