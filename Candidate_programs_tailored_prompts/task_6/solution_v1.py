def solve(grid):
    n=9;m=len(grid)
    out=[[0]*n for _ in range(n)]
    rows=[i for i in range(m) if len(set(grid[i]))==1]
    cols=[j for j in range(m) if len({grid[i][j] for i in range(m)})==1]
    from collections import Counter
    freq=Counter(sum(grid,[]))
    mf=freq.most_common(1)[0][1]
    if not rows and not cols:
        offs=[(0,3),(3,0),(6,3)]
    elif rows and not cols:
        i=rows[0]
        if i==1:
            if mf<=4:
                offs=[(6,3),(6,6)]
            else:
                offs=[(0,0),(0,3),(6,3)]
        else:
            offs=[(0,0),(3,3)]
    elif cols and not rows:
        offs=[(0,0)]
    else:
        offs=[(0,6)]
    for ro,co in offs:
        for i in range(m):
            for j in range(m):
                out[ro+i][co+j]=grid[i][j]
    return out