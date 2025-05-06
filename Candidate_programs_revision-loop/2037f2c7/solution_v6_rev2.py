from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0])
    def comps_of_color(v):
        seen=[[False]*w for _ in range(h)]
        comps=[]
        for i in range(h):
            for j in range(w):
                if grid[i][j]==v and not seen[i][j]:
                    q=deque([(i,j)])
                    seen[i][j]=True
                    comp=[]
                    while q:
                        r,c=q.popleft()
                        comp.append((r,c))
                        for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
                            nr, nc = r+dr, c+dc
                            if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==v:
                                seen[nr][nc]=True
                                q.append((nr,nc))
                    comps.append(comp)
        return comps
    def make_mat(comp):
        rs=[r for r,c in comp]; cs=[c for r,c in comp]
        r0,r1,c0,c1=min(rs),max(rs),min(cs),max(cs)
        H,W=r1-r0+1,c1-c0+1
        m=[[False]*W for _ in range(H)]
        for r,c in comp:
            m[r-r0][c-c0]=True
        return m,H,W
    def rotate90(m):
        H,W=len(m),len(m[0])
        return [[m[H-1-r][c] for r in range(H)] for c in range(W)]
    def flip_h(m):
        return [row[::-1] for row in m]
    def flip_v(m):
        return m[::-1]
    for v in range(1,10):
        cs=comps_of_color(v)
        if len(cs)!=2: continue
        A,B=cs
        arr1,h1,w1=make_mat(A)
        arr2,h2,w2=make_mat(B)
        best=None; best_cnt=-1
        trans=[]
        m0=arr2
        trans.append(m0)
        trans.append(flip_h(m0))
        trans.append(flip_v(m0))
        r90=rotate90(m0)
        trans.append(r90)
        trans.append(rotate90(r90))
        trans.append(rotate90(rotate90(r90)))
        trans.append(flip_h(r90))
        trans.append(flip_v(r90))
        for m2 in trans:
            ht,wt=len(m2),len(m2[0])
            off_r=(h1-ht)//2; off_c=(w1-wt)//2
            inter=[]
            for i in range(ht):
                for j in range(wt):
                    if m2[i][j]:
                        r0=i+off_r; c0=j+off_c
                        if 0<=r0<h1 and 0<=c0<w1 and arr1[r0][c0]:
                            inter.append((r0,c0))
            if not inter: continue
            rr=[r for r,c in inter]; cc=[c for r,c in inter]
            rmin,rmax,minc,maxc=min(rr),max(rr),min(cc),max(cc)
            cnt=len(inter)
            if cnt>best_cnt:
                best_cnt=cnt
                mat=[ [8 if (i+ rmin,j+minc) in [(x,y) for x,y in inter] else 0 for j in range(maxc-minc+1)] for i in range(rmin,rmax+1) ]
                best=mat
        if best is not None:
            return best
    return []