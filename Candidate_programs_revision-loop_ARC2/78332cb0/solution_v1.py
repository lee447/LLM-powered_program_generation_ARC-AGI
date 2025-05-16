from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n=len(grid); m=len(grid[0])
    rseps=[i for i,row in enumerate(grid) if all(v==6 for v in row)]
    cseps=[j for j in range(m) if all(grid[i][j]==6 for i in range(n))]
    row_blocks=[]
    prev=0
    for r in rseps:
        if prev<r: row_blocks.append((prev,r))
        prev=r+1
    if prev<n: row_blocks.append((prev,n))
    col_blocks=[]
    prev=0
    for c in cseps:
        if prev<c: col_blocks.append((prev,c))
        prev=c+1
    if prev<m: col_blocks.append((prev,m))
    panels=[[ [row[c0:c1] for row in grid[r0:r1]] for (c0,c1) in col_blocks] for (r0,r1) in row_blocks]
    nr=len(row_blocks); nc=len(col_blocks)
    out=[]
    if nr>1 and nc>1:
        seq=[]
        for i in range(nr):
            if i<nc: seq.append(panels[i][i])
        for i in range(nr):
            j=nc-1-i
            if 0<=j<nc and i!=j: seq.append(panels[i][j])
        pw=len(panels[0][0][0])
        for idx,p in enumerate(seq):
            for row in p: out.append(list(row))
            if idx<len(seq)-1: out.append([6]*pw)
    elif nr>1 and nc==1:
        pls=[panels[i][0] for i in range(nr)]
        seq=list(reversed(pls))
        ph=len(pls[0]); pw=len(pls[0][0])
        for r in range(ph):
            row=[]
            for idx,p in enumerate(seq):
                if idx>0: row.append(6)
                row+=p[r]
            out.append(row)
    elif nr==1 and nc>1:
        pls=panels[0]
        seq=pls
        ph=len(pls[0]); pw=len(pls[0][0])
        for idx,p in enumerate(seq):
            for row in p: out.append(list(row))
            if idx<len(seq)-1: out.append([6]*pw)
    else:
        return grid
    return out