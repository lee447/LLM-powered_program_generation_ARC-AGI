def solve(grid):
    H=len(grid);W=len(grid[0])
    bar_rows=[]
    for r in range(H):
        for j in range(W):
            if grid[r][j]!=0 and ((j-1>=0 and grid[r][j-1]==grid[r][j]) or (j+1<W and grid[r][j+1]==grid[r][j])):
                bar_rows.append(r)
                break
    bar_rows=sorted(set(bar_rows))
    axes=set()
    for r in range(H):
        if r not in bar_rows:
            for j in range(W):
                if grid[r][j]!=0:
                    axes.add(j)
    axes=sorted(axes)
    neighbor={}
    for c in axes:
        lst=[]
        for r in bar_rows:
            if grid[r][c]!=0:
                col=grid[r][c]
            else:
                col=None
                if c-1>=0 and grid[r][c-1]!=0: col=grid[r][c-1]
                elif c+1<W and grid[r][c+1]!=0: col=grid[r][c+1]
            if col is not None:
                lst.append((r,col))
        lst.sort()
        neighbor[c]=lst
    new=[[0]*W for _ in range(H)]
    top_max=bar_rows[-1] if bar_rows else -1
    for r in range(H):
        if r>top_max:
            for j in range(W):
                if grid[r][j]!=0:
                    new[r][j]=grid[r][j]
        else:
            if r in bar_rows:
                colors=set(v for v in grid[r] if v!=0)
                for col in colors:
                    idxs=[j for j in range(W) if grid[r][j]==col]
                    mi,ma=min(idxs),max(idxs)
                    for j in range(mi,ma+1):
                        new[r][j]=col
            for c in axes:
                lst=neighbor[c]
                col_val=lst[-1][1]
                for rr,cc in lst:
                    if rr>=r:
                        col_val=cc
                        break
                new[r][c]=col_val
    return new