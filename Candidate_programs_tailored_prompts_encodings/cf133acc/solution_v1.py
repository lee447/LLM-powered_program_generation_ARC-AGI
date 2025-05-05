def solve(grid):
    H=len(grid);W=len(grid[0])
    counts=[sum(1 for r in range(H) if grid[r][c]!=0) for c in range(W)]
    axes=[c for c in range(W) if counts[c]>1]
    axes.sort()
    c0,c1=axes[0],axes[1]
    bar_rows=[r for r in range(H) if any(grid[r][c]!=0 and c not in (c0,c1) for c in range(W))]
    bar_rows.sort()
    mid_idx=len(bar_rows)//2
    mid_row=bar_rows[mid_idx]
    new=[[0]*W for _ in range(H)]
    for c in range(W):
        if c not in (c0,c1):
            new[mid_row][c]=grid[mid_row][c]
    below=[r for r in bar_rows if r>mid_row]
    for r in below:
        for c in range(W):
            if c in (c0,c1):
                v=0
                if c-1>=0 and grid[r][c-1]!=0: v=grid[r][c-1]
                elif c+1<W and grid[r][c+1]!=0: v=grid[r][c+1]
                new[r][c]=v
            else:
                new[r][c]=grid[r][c]
    axis_vals0=[grid[r][c0] for r in range(mid_row+1,H) if grid[r][c0]!=0 and r not in bar_rows]
    axis_vals1=[grid[r][c1] for r in range(mid_row+1,H) if grid[r][c1]!=0 and r not in bar_rows]
    for i,v in enumerate(axis_vals0):
        new[mid_row+1+i][c0]=v
    for i,v in enumerate(axis_vals1):
        new[mid_row+1+i][c1]=v
    above=[r for r in bar_rows if r<mid_row]
    def extract(axis):
        segs=[]
        for r in sorted(above, key=lambda x:mid_row-x):
            if axis-1>=0 and grid[r][axis-1]!=0:
                color=grid[r][axis-1];l=0
                while axis-1-l>=0 and grid[r][axis-1-l]==color: l+=1
                segs.append((l,color))
            elif axis+1<W and grid[r][axis+1]!=0:
                color=grid[r][axis+1];l=0
                while axis+1+l<W and grid[r][axis+1+l]==color: l+=1
                segs.append((l,color))
        return segs
    seg0=extract(c0);seg1=extract(c1)
    off0=0
    for l,v in seg0:
        for k in range(l):
            new[mid_row-1-off0-k][c0]=v
        off0+=l
    off1=0
    for l,v in seg1:
        for k in range(l):
            new[mid_row-1-off1-k][c1]=v
        off1+=l
    return new