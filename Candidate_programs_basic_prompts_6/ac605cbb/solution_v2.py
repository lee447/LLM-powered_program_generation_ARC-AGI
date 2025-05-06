def solve(grid):
    h=len(grid); w=len(grid[0])
    pts=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0:
                pts.append((i,j,grid[i][j]))
    out=[[0]*w for _ in range(h)]
    def draw_L(a,b,c,col,fill):
        ai,aj=a; bi,bj=b
        di = 1 if bi>ai else -1 if bi<ai else 0
        dj = 1 if bj>aj else -1 if bj<aj else 0
        x,y=ai,aj
        for _ in range(abs(bj-aj)):
            y+=dj; out[x][y]=fill
        for _ in range(abs(bi-ai)):
            x+=di; out[x][y]=fill
        out[x][y]=col
    def mirror(p):
        i,j,c=p
        mi=h-1-i; mj=w-1-j
        return (mi,mj,c)
    if len(pts)==1:
        p=pts[0]
        m=mirror(p)
        draw_L(p,m,p[2],p[2],5)
    else:
        n=len(pts)
        for i in range(n):
            a=pts[i]
            b=pts[(i+1)%n]
            draw_L(a,b,a[2],a[2],5)
    return out