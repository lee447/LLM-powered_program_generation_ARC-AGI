def solve(grid):
    h=len(grid); w=len(grid[0])
    bg=8; fill=3
    bands=[]
    i=0
    while i<h:
        if any(grid[i][j]!=bg and grid[i][j]!=6 for j in range(w)):
            start=i
            while i<h and any(grid[i][j]!=bg and grid[i][j]!=6 for j in range(w)): i+=1
            bands.append((start,i-1))
        else:
            i+=1
    out=[row[:]for row in grid]
    for bi,(r0,r1) in enumerate(bands):
        if bi%2==0:
            for r in range(r0-1,r1+2):
                if 0<=r<h and all(grid[r][c]!=6 for c in range(w)):
                    for c in range(w):
                        if out[r][c]==bg: out[r][c]=fill
            for r in range(r0,r1+1):
                for c in range(w):
                    if out[r][c]==bg: out[r][c]=fill
    return out