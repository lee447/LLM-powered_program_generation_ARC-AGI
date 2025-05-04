def solve(grid):
    m=len(grid); n=len(grid[0])
    for i in range(m):
        row=grid[i]
        if 2 not in row and len(set(row))==1:
            above=any(2 in grid[r] for r in range(i))
            below=any(2 in grid[r] for r in range(i+1,m))
            if above and below:
                border_type='row'; idx=i; break
    else:
        for j in range(n):
            col=[grid[i][j] for i in range(m)]
            if 2 not in col and len(set(col))==1:
                left=any(2 in grid[r][:j] for r in range(m))
                right=any(2 in grid[r][j+1:] for r in range(m))
                if left and right:
                    border_type='col'; idx=j; break
    zones=[]
    if border_type=='row':
        zones=[(0,idx-1,0,n-1),(idx+1,m-1,0,n-1)]
    else:
        zones=[(0,m-1,0,idx-1),(0,m-1,idx+1,n-1)]
    blocks=[]
    bg=[]
    for zi,(rmin,rmax,cmin,cmax) in enumerate(zones):
        b=None
        for r in range(rmin,rmax+1):
            for c in range(cmin,cmax+1):
                if grid[r][c]!=2:
                    b=grid[r][c]; break
            if b is not None: break
        bg.append(b)
        for r in range(rmin,rmax):
            for c in range(cmin,cmax):
                if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                    blocks.append((zi,r,c))
    for zi,r,c in blocks:
        for dr in (0,1):
            for dc in (0,1):
                grid[r+dr][c+dc]=bg[zi]
    for zi,r,c in blocks:
        rmin,rmax,cmin,cmax=zones[zi]
        if bg[zi]==1:
            newc=cmax-1
        else:
            newc=cmin
        for dr in (0,1):
            for dc in (0,1):
                grid[r+dr][newc+dc]=2
    return grid