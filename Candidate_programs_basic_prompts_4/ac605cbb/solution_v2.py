def solve(grid):
    h=len(grid); w=len(grid[0])
    pts=[]
    for y in range(h):
        for x in range(w):
            if grid[y][x]!=0:
                pts.append((y,x,grid[y][x]))
    out=[row[:] for row in grid]
    def sign(a): return 1 if a>0 else -1 if a<0 else 0
    def draw_path(p1,p2):
        y1,x1,_=p1; y2,x2,_=p2
        dy=y2-y1; dx=x2-x1
        ady,adx=abs(dy),abs(dx)
        if adx<ady:
            order=[(0,sign(dx))]*adx+[(sign(dy),0)]*ady
        else:
            order=[(sign(dy),0)]*ady+[(0,sign(dx))]*adx
        y,x=y1,x1
        for dy0,dx0 in order[:-1]:
            y+=dy0; x+=dx0
            if out[y][x]==0: out[y][x]=5
    def mirror(p1,p2):
        y1,x1,c1=p1; y2,x2,c2=p2
        dy=y2-y1; dx=x2-x1
        sdy,sdx=sign(dy),sign(dx)
        ady,adx=abs(dy),abs(dx)
        # mirror p1
        if adx==0:
            m1=(y1-ady,x1)
        elif ady==0:
            m1=(y1,x1-adx)
        else:
            m1=(y1-sdy, x1+dx)
        # mirror p2
        if adx==0:
            m2=(y2+ady,x2)
        elif ady==0:
            m2=(y2,x2+adx)
        else:
            m2=(y2+dy, x2-sdx)
        return (m1[0],m1[1],c1),(m2[0],m2[1],c2)
    if len(pts)==1:
        p=pts[0]
        m=(h-1-p[0],p[1],p[2])
        draw_path(p,m)
        out[p[0]][p[1]]=p[2]
        out[m[0]][m[1]]=p[2]
    else:
        pts_sorted=sorted(pts)
        for i in range(len(pts_sorted)-1):
            p1=pts_sorted[i]; p2=pts_sorted[i+1]
            draw_path(p1,p2)
            out[p1[0]][p1[1]]=p1[2]
            out[p2[0]][p2[1]]=p2[2]
            m1,m2=mirror(p1,p2)
            if 0<=m1[0]<h and 0<=m1[1]<w: out[m1[0]][m1[1]]=m1[2]
            if 0<=m2[0]<h and 0<=m2[1]<w: out[m2[0]][m2[1]]=m2[2]
    return out