def solve(grid):
    H=len(grid);W=len(grid[0])
    pts=[(i,j) for i in range(H) for j in range(W) if grid[i][j]==4]
    def is_elbow(i,j):
        nbr=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        c=[(ni,nj) for ni,nj in nbr if 0<=ni<H and 0<=nj<W and grid[ni][nj]==4]
        if len(c)!=2: return False
        return not (c[0][0]==c[1][0] or c[0][1]==c[1][1])
    pivots=[(i,j) for i,j in pts if is_elbow(i,j)]
    pi,pj=pivots[0]
    offs=[(i-pi,j-pj) for i,j in pts]
    M=max(max(abs(di),abs(dj)) for di,dj in offs)
    D=4*M+3
    C=D//2
    out=[[0]*D for _ in range(D)]
    for di,dj in offs:
        for k in range(4):
            if k==0: x,y=di,dj
            elif k==1: x,y=dj,-di
            elif k==2: x,y=-di,-dj
            else: x,y=-dj,di
            out[C+x][C+y]=4
    return out