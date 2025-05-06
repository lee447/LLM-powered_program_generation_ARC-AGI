def solve(grid):
    h=len(grid);w=len(grid[0]);bs=h
    res=[[0]*w for _ in range(h)]
    diag1={(i,i) for i in range(bs)}
    diag2={(i,bs-1-i) for i in range(bs)}
    for b in range(w//bs):
        pos={(i,j) for i in range(bs) for j in range(bs) if grid[i][b*bs+j]==5}
        if len(pos)==1:
            c=4
        elif len(pos)==8:
            c=3
        elif pos==diag1 or pos==diag2:
            c=9
        elif all(i==0 for i,j in pos):
            c=6
        else:
            c=1
        for i in range(bs):
            for j in range(bs):
                res[i][b*bs+j]=c
    return res