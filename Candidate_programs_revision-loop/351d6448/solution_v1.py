def solve(grid):
    rows=len(grid);cols=len(grid[0])
    grey_rows=[r for r in range(rows) if all(grid[r][c]==5 for c in range(cols))]
    starts=[];lengths=[];shapes=[]
    for gr in grey_rows:
        r=gr-1
        in_run=False
        for c in range(cols):
            if grid[r][c]!=0 and not in_run:
                start=c;in_run=True
            if (grid[r][c]==0 or c==cols-1) and in_run:
                end=c-1 if grid[r][c]==0 else c
                shapes.append([grid[r][i] for i in range(start,end+1)])
                starts.append(start);lengths.append(end-start+1)
                in_run=False
    n=len(starts)
    if n>1:
        ds=(starts[-1]-starts[0])//(n-1)
        dl=(lengths[-1]-lengths[0])//(n-1)
    else:
        ds=dl=0
    nxt_start=starts[0]+n*ds
    nxt_len=lengths[0]+n*dl
    base=shapes[0]
    if len(set(base))==1:
        fill=[base[0]]*nxt_len
    else:
        fill=base
    out=[[0]*cols for _ in range(3)]
    out[1][nxt_start:nxt_start+nxt_len]=fill
    return out