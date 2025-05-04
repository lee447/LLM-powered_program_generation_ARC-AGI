def solve(grid):
    h=len(grid); w=len(grid[0])
    b=0
    for i,row in enumerate(grid):
        if all(v==5 for v in row):
            b=i
            break
    def max_run(color, r0, r1):
        m=0
        for j in range(w):
            c=0
            for i in range(r0, r1):
                if grid[i][j]==color:
                    c+=1
                    if c>m: m=c
                else:
                    c=0
        return m
    best=None
    best_diff=-1
    for color in (2,4):
        a=max_run(color,0,b)
        c=max_run(color,b+1,h)
        d=abs(c-a)
        if d>best_diff:
            best_diff=d
            best=color
    return [[best,best],[best,best]]