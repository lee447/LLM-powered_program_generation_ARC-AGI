def solve(grid):
    vals=[(r,c) for r,row in enumerate(grid) for c,v in enumerate(row) if v!=0]
    if not vals: return grid
    rs=[r for r,c in vals]; cs=[c for r,c in vals]
    r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
    h=r1-r0+1; w=maxc-minc+1
    sub=[row[minc:maxc+1] for row in grid[r0:r1+1]]
    s=max(h,w)
    rt=(s-h)//2; rb=s-h-rt
    cl=(s-w)//2; cr=s-w-cl
    tile=[[0]*s for _ in range(s)]
    for i in range(h):
        for j in range(w):
            tile[i+rt][j+cl]=sub[i][j]
    def rot(mat):
        return [ [mat[s-1-j][i] for j in range(s)] for i in range(s) ]
    G=[[0]*(3*s) for _ in range(3*s)]
    offs=[(0,s),(s,2*s),(2*s,s),(s,0)]
    T=tile
    for k in range(4):
        dx,dy=offs[k]
        for i in range(s):
            for j in range(s):
                if T[i][j]!=0:
                    G[dx+i][dy+j]=T[i][j]
        T=rot(T)
    # trim bottom zero rows
    while G and all(x==0 for x in G[-1]):
        G.pop()
    # trim right zero cols
    if G:
        m=len(G[0])
        while m>0 and all(row[m-1]==0 for row in G):
            for row in G: row.pop()
            m-=1
    return G