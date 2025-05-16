from collections import Counter
def solve(grid):
    h,w=len(grid),len(grid[0])
    cnt=Counter(x for r in grid for x in r)
    bg=cnt.most_common(1)[0][0]
    wall=[c for c,_ in cnt.most_common() if c!=bg][0]
    col_walls=[j for j in range(w) if all(grid[i][j]==wall for i in range(h))]
    if len(col_walls)>=2:
        l,r=col_walls[0],col_walls[1]
        out=[]
        for i in range(h):
            row=grid[i][l:r+1]
            new=row[:]
            for j in range(len(row)):
                if row[j]==bg:
                    best=None;bd=10**9
                    for k in range(len(row)):
                        if row[k]!=bg and row[k]!=wall:
                            d=abs(k-j)
                            if d<bd:
                                bd, best=d,row[k]
                    new[j]=best if best is not None else row[j]
            out.append(new)
        return out
    row_walls=[i for i in range(h) if all(grid[i][j]==wall for j in range(w))]
    if len(row_walls)>=2:
        top,bottom=row_walls[0],row_walls[1]
        out=[]
        for i in range(top,bottom+1):
            out.append([wall if v==bg else v for v in grid[i]])
        return out
    return grid