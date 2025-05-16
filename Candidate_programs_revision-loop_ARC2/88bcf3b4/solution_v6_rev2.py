from collections import Counter
def solve(grid):
    h,len0=len(grid),len(grid[0])
    cnt=Counter(c for row in grid for c in row)
    bg,=sorted(cnt.items(), key=lambda x:-x[1])[:1]
    bg=bg[0]
    shapes={c:[] for c in cnt if c!=bg}
    for i in range(h):
        for j in range(len0):
            c=grid[i][j]
            if c in shapes:
                shapes[c].append((i,j))
    def endpoints(pts):
        s=set(pts)
        res=[]
        for p in pts:
            nb=0
            for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (p[0]+d[0],p[1]+d[1]) in s:
                    nb+=1
            if nb==1:
                res.append(p)
        return res
    def rotate_once(pts,piv):
        pr,pc=piv; out=[]
        for r,c in pts:
            dr,dc=r-pr,c-pc
            out.append((pr+dc,pc-dr))
        return out
    def rotate(pts,piv,k):
        r=pts
        for _ in range(k):
            r=rotate_once(r,piv)
        return r
    colors_sorted=sorted(shapes, key=lambda c: len(shapes[c]))
    Scol,Mcol,Lcol=colors_sorted
    Spts, Mpts, Lpts = shapes[Scol], shapes[Mcol], shapes[Lcol]
    # endpoints
    EpM= endpoints(Mpts)
    EpL= endpoints(Lpts)
    setL=set(Lpts)
    # attach M to L
    placedM=None
    for eL in EpL:
        otherL = EpL[1] if EpL[0]==eL else EpL[0]
        drL,dcL=otherL[0]-eL[0],otherL[1]-eL[1]
        if drL!=0: drL=drL//abs(drL); dcL=0
        else: dcL=dcL//abs(dcL); drL=0
        pvL=(dcL,-drL)
        for eM in EpM:
            for k in range(4):
                rm=rotate(Mpts,eM,k)
                delta=(eL[0]-eM[0],eL[1]-eM[1])
                rm2=[(r+delta[0],c+delta[1]) for r,c in rm]
                srm=set(rm2)
                if eL not in srm: continue
                if len(srm & setL)!=1: continue
                ok=True
                for p in rm2:
                    if p!=eL and (p[0]-eL[0])*pvL[0]+(p[1]-eL[1])*pvL[1] <=0:
                        ok=False; break
                if ok:
                    placedM=srm; break
            if placedM: break
        if placedM: break
    # attach S to M
    EpM2=list(p for p in placedM if sum((abs(p[0]-q[0])+abs(p[1]-q[1])==1) for q in placedM)==1)
    placedS=None
    for eM2 in EpM2:
        otherM2 = EpM2[1] if EpM2[0]==eM2 else EpM2[0]
        drM,dcM=otherM2[0]-eM2[0],otherM2[1]-eM2[1]
        if drM!=0: drM=drM//abs(drM); dcM=0
        else: dcM=dcM//abs(dcM); drM=0
        pvM=(dcM,-drM)
        EpS=endpoints(Spts)
        for eS in EpS:
            for k in range(4):
                rs=rotate(Spts,eS,k)
                delta=(eM2[0]-eS[0],eM2[1]-eS[1])
                rs2=[(r+delta[0],c+delta[1]) for r,c in rs]
                srs=set(rs2)
                if eM2 not in srs: continue
                if len(srs & placedM)!=1: continue
                if srs & setL: continue
                ok=True
                for p in rs2:
                    if p!=eM2 and (p[0]-eM2[0])*pvM[0]+(p[1]-eM2[1])*pvM[1] <=0:
                        ok=False; break
                if ok:
                    placedS=srs; break
            if placedS: break
        if placedS: break
    new=[[bg]*len0 for _ in range(h)]
    for r,c in Lpts: new[r][c]=Lcol
    for r,c in placedM: new[r][c]=Mcol
    for r,c in placedS: new[r][c]=Scol
    return new