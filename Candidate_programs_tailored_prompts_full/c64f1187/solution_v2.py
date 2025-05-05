def solve(grid):
    h=len(grid); w=len(grid[0])
    block=2; gap=1
    anchorRow=next(i for i,row in enumerate(grid) if any(v not in (0,1,5) for v in row))
    greyStarts=[]
    for i in range(h-1):
        if any(grid[i][j]==5 for j in range(w)) and any(grid[i+1][j]==5 for j in range(w)):
            if i==0 or not any(grid[i-1][j]==5 for j in range(w)):
                greyStarts.append(i)
    c_list=[]
    r0=greyStarts[0]
    for j in range(w-1):
        if grid[r0][j]==5 and grid[r0][j+1]==5 and grid[r0+1][j]==5 and grid[r0+1][j+1]==5:
            c_list.append(j)
    c_list=sorted(c_list)
    dGrey=min(c_list[i+1]-c_list[i] for i in range(len(c_list)-1)) if len(c_list)>1 else 1
    minC=c_list[0]
    rGrey=[(c-minC)//dGrey for c in c_list]
    width=max(rGrey)*(block+gap)+block
    if anchorRow==0:
        bandStarts=[('anchor',anchorRow)]+[('insert',r) for r in greyStarts[1:]]
    else:
        bandStarts=[('insert',r) for r in greyStarts]
    B=len(bandStarts)
    H=B*(block+gap)-gap
    out=[[0]*width for _ in range(H)]
    for bi,(tp,rstart) in enumerate(bandStarts):
        out_r=bi*(block+gap)
        if tp=='anchor':
            anchors=[(j,grid[rstart][j]) for j in range(w) if grid[rstart][j] not in (0,1,5)]
            anchors.sort()
            if len(anchors)>1:
                dA=min(anchors[i+1][0]-anchors[i][0] for i in range(len(anchors)-1))
            else:
                dA=1
            minA=anchors[0][0]
            for c,v in anchors:
                ri=(c-minA)//dA
                off=ri*(block+gap)
                for dr in (0,1):
                    for dc in (0,1):
                        out[out_r+dr][off+dc]=v
        else:
            for c in c_list:
                val=0
                for dr in (0,1):
                    for dc in (0,1):
                        v=grid[rstart+dr][c+dc]
                        if v not in (0,5):
                            val=v
                if val:
                    ri=(c-minC)//dGrey
                    off=ri*(block+gap)
                    for dr in (0,1):
                        for dc in (0,1):
                            out[out_r+dr][off+dc]=val
    return out