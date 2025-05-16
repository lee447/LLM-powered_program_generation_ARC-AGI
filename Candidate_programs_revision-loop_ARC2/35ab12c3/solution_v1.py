def solve(grid):
    h=len(grid); w=len(grid[0])
    pos={}
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            if c:
                pos.setdefault(c,[]).append((i,j))
    out=[[0]*w for _ in range(h)]
    used=set()
    def draw_diamond(center, r, border, fill):
        cr,cc=center
        for i in range(h):
            for j in range(w):
                d=abs(i-cr)+abs(j-cc)
                if d==r and out[i][j]==0:
                    out[i][j]=border
                elif d<r and fill and out[i][j]==0:
                    out[i][j]=fill
    def draw_line(a,b,color):
        (r1,c1),(r2,c2)=a,b
        if r1==r2:
            for j in range(min(c1,c2),max(c1,c2)+1):
                out[r1][j]=color
        else:
            for i in range(min(r1,r2),max(r1,r2)+1):
                out[i][c1]=color
    def draw_rect(rmin,rmax,cmin,cmax,border,fill):
        for j in range(cmin,cmax+1):
            if out[rmin][j]==0: out[rmin][j]=border
            if out[rmax][j]==0: out[rmax][j]=border
        for i in range(rmin,rmax+1):
            if out[i][cmin]==0: out[i][cmin]=border
            if out[i][cmax]==0: out[i][cmax]=border
        for i in range(rmin+1,rmax):
            for j in range(cmin+1,cmax):
                if fill and out[i][j]==0:
                    out[i][j]=fill
    # diamond1: one 7 single -> nearest partner
    if 7 in pos and len(pos[7])==1:
        p7=pos[7][0]
        best=None; bd=10**9
        for c,pts in pos.items():
            if c!=7 and len(pts)==1:
                d=abs(pts[0][0]-p7[0])+abs(pts[0][1]-p7[1])
                if d<bd:
                    bd=d; best=(c,pts[0])
        if best:
            fill,pc=best; border=7; center=pc; r=bd
            draw_diamond(center,r,border,fill)
            used.update({7,fill})
    # diamond2: border 7 cluster symmetric
    if 7 in pos and pos[7] and len(pos[7])>1 and 7 not in used:
        rs=[i for i,_ in pos[7]]; cs=[j for _,j in pos[7]]
        rmin,rmax=min(rs),max(rs)
        cmin,cmax=min(cs),max(cs)
        if rmax-rmin==cmax-cmin and (rmax-rmin)%2==0:
            r=(rmax-rmin)//2
            center=((rmax+rmin)//2,(cmax+cmin)//2)
            draw_diamond(center,r,7,0)
            used.add(7)
    # lines
    for c,pts in pos.items():
        if c not in used and len(pts)==2:
            a,b=pts
            if a[0]==b[0] or a[1]==b[1]:
                draw_line(a,b,c)
                used.add(c)
    # rectangle-other: one single and one big >3
    singles=[c for c,pts in pos.items() if c not in used and len(pts)==1]
    bigs=[c for c,pts in pos.items() if c not in used and len(pts)>3]
    if len(singles)==1 and len(bigs)==1:
        d=singles[0]; c=bigs[0]
        pts=pos[c]
        rows=[i for i,_ in pts]+[pos[d][0][0]]
        cols=[j for _,j in pts]+[pos[d][0][1]]
        rmin,rmax=min(rows),max(rows)
        cmin,cmax=min(cols),max(cols)
        draw_rect(rmin,rmax,cmin,cmax,c,d)
        used.update({c,d})
    # rectangle1: color corner size4 with other single
    for c,pts in pos.items():
        if c not in used and len(pts)==4:
            rs=[i for i,_ in pts]; cs=[j for _,j in pts]
            rmin,rmax=min(rs),max(rs)
            cmin,cmax=min(cs),max(cs)
            corners={(rmin,cmin),(rmin,cmax),(rmax,cmin),(rmax,cmax)}
            if set(pts)==corners:
                others=[d for d in pos if d not in used and d!=c and len(pos[d])==1]
                if others:
                    d=others[0]
                    draw_rect(rmin,rmax,cmin,cmax,d,c)
                    used.update({c,d})
    # overlay originals
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0:
                out[i][j]=grid[i][j]
    return out