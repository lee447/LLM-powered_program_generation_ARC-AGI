def solve(grid):
    H=len(grid);W=len(grid[0])
    res=[[0]*W for _ in range(H)]
    reds=[(r,c) for r in range(H) for c in range(W) if grid[r][c]==2]
    for r,c in reds:res[r][c]=2
    for r,c in reds:
        cnt=0
        for dr,dc in((-1,0),(1,0),(0,-1),(0,1)):
            if (r+dr,c+dc) in reds:cnt+=1
        if cnt==4:
            cr,cc=r,c
            break
    arms=[(cr+dr,cc+dc)for dr,dc in((-1,0),(1,0),(0,-1),(0,1))]
    corners=[(cr-1,cc-1),(cr-1,cc+1),(cr+1,cc-1),(cr+1,cc+1)]
    for pr,pc in corners:
        dr=pr-cr;dc=pc-cc
        sr=1 if dr>0 else -1; sc=1 if dc>0 else -1
        r,c=pr,pc
        while 0<=r<H and 0<=c<W:
            if not (grid[r][c]==2 or res[r][c]!=0):
                res[r][c]=1
            r+=sr; c+=sc
    for dr,dc in((-2,0),(2,0),(0,-2),(0,2)):
        r,c=cr+dr,cc+dc
        if 0<=r<H and 0<=c<W and res[r][c]==0 and grid[r][c]!=2:
            res[r][c]=8
    for r in range(H):
        if grid[r][cc]==2 or res[r][cc]!=0:continue
        res[r][cc]=4 if r==0 or r==H-1 else 8
    for c in range(W):
        if grid[cr][c]==2 or res[cr][c]!=0:continue
        res[cr][c]=4 if c==0 or c==W-2 else 8
    return res