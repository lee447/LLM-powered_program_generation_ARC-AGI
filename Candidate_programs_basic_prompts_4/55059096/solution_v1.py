def solve(grid):
    h=len(grid); w=len(grid[0])
    new=[row[:] for row in grid]
    centers=[]
    for i in range(1,h-1):
        for j in range(1,w-1):
            if grid[i][j]==3 and grid[i-1][j]==3 and grid[i+1][j]==3 and grid[i][j-1]==3 and grid[i][j+1]==3:
                centers.append((i,j))
    for a in range(len(centers)):
        i1,j1=centers[a]
        for b in range(a+1,len(centers)):
            i2,j2=centers[b]
            di=i2-i1; dj=j2-j1
            if abs(di)==abs(dj) and di!=0:
                si=1 if di>0 else -1; sj=1 if dj>0 else -1
                for t in range(1,abs(di)):
                    r=i1+si*t; c=j1+sj*t
                    if new[r][c]!=3:
                        new[r][c]=2
    return new