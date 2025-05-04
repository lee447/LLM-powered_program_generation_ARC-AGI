def solve(grid):
    h=len(grid);w=len(grid[0])
    cnt={}
    for r in range(h):
        for c in range(w):
            v=grid[r][c]
            if v!=0:
                cnt[v]=cnt.get(v,0)+1
    items=sorted(cnt.items(),key=lambda x:-x[1])
    inside=items[0][0]
    outside=items[1][0] if len(items)>1 else inside
    res=[row[:] for row in grid]
    r=1
    while r+4<h:
        c=1
        while c+4<w:
            for i in range(5):
                for j in range(5):
                    if abs(i-2)+abs(j-2)<=2:
                        res[r+i][c+j]=inside
                    else:
                        res[r+i][c+j]=outside
            c+=6
        r+=6
    return res