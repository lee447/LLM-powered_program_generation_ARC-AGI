def solve(grid):
    h,len_row=len(grid),len(grid[0])
    cnt={}
    for r in grid:
        for v in r:
            cnt[v]=cnt.get(v,0)+1
    bg=max(cnt,key=lambda k:cnt[k])
    pos_by_color={}
    for i in range(h):
        for j in range(len_row):
            v=grid[i][j]
            if v!=bg:
                pos_by_color.setdefault(v,[]).append((i,j))
    ref_color=max(pos_by_color,key=lambda k:len(pos_by_color[k]))
    P=pos_by_color[ref_color]
    minr=min(r for r,c in P);minc=min(c for r,c in P)
    P_norm=[(r-minr,c-minc)for r,c in P]
    def rot(p):
        r,c=p;return (c,-r)
    Rks=[]
    cur=P_norm
    for _ in range(4):
        rs=[rot(p)for p in cur]
        mr=min(r for r,c in rs);mc=min(c for r,c in rs)
        norm=[(r-mr,c-mc)for r,c in rs]
        Rks.append(norm)
        cur=rs
    out=[[bg]*len_row for _ in range(h)]
    for v,pts in pos_by_color.items():
        S=set(pts)
        for R in Rks:
            Rset=set(R)
            for pr in R:
                tr,tc=pts[0][0]-pr[0],pts[0][1]-pr[1]
                if all((r-tr,c-tc) in Rset for r,c in S):
                    for r0,c0 in R:
                        r,c=r0+tr,c0+tc
                        out[r][c]=v
                    break
            else:
                continue
            break
    return out