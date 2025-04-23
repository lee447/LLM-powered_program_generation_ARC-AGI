def solve(grid):
    n,r=len(grid),len(grid)
    m=len(grid[0])
    # locate anchor color
    cnt8=sum(cell==8 for row in grid for cell in row)
    anchor_color=8 if cnt8>0 else 9
    # find bounding box
    rows=[i for i in range(n) for j in range(m) if grid[i][j]==anchor_color]
    cols=[j for i in range(n) for j in range(m) if grid[i][j]==anchor_color]
    r0,r1=min(rows),max(rows)
    c0,c1=min(cols),max(cols)
    h,w=r1-r0+1,c1-c0+1
    # count noisy on each side
    noisy_left=sum(1 for i in range(r0,r1+1) for j in range(c0) if grid[i][j] in (6,7))
    noisy_right=sum(1 for i in range(r0,r1+1) for j in range(c1+1,m) if grid[i][j] in (6,7))
    # choose side of neighbor
    if noisy_left>noisy_right:
        dc=-1
    else:
        dc=1
    # extract patch
    out=[[grid[r0+i][c0+j+dc] for j in range(w)] for i in range(h)]
    return out