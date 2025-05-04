def solve(grid):
    h=len(grid); w=len(grid[0])
    g2=[row[:] for row in grid]
    cnt={}
    for r in range(h):
        for c in range(w):
            cnt[grid[r][c]]=cnt.get(grid[r][c],0)+1
    best_area=0; X=None
    for col,ct in cnt.items():
        coords=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==col]
        if not coords: continue
        minr=min(r for r,c in coords); maxr=max(r for r,c in coords)
        minc=min(c for r,c in coords); maxc=max(c for r,c in coords)
        area=(maxr-minr+1)*(maxc-minc+1)
        if area==len(coords) and area>best_area:
            best_area=area; X=col
    if X is None:
        return g2
    coords=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==X]
    minr=min(r for r,c in coords); maxr=max(r for r,c in coords)
    minc=min(c for r,c in coords); maxc=max(c for r,c in coords)
    H=maxr-minr+1; W=maxc-minc+1
    n=max(H,W)
    ar1=minr; ar2=minr+n
    if ar2>=h:
        ar1=maxr-n; ar2=maxr
    ac1=minc; ac2=minc+n
    if ac2>=w:
        ac1=maxc-n; ac2=maxc
    A=[ [grid[r][c] for c in range(ac1,ac2+1)] for r in range(ar1,ar2+1) ]
    N=len(A)
    for d in range(N-1,0,-1):
        for i in range(N-d):
            j=i+d
            v1=A[i][j]; v2=A[j][i]
            if v1!=X and v2==X:
                v=v1
            elif v2!=X and v1==X:
                v=v2
            else:
                v=v1
            A[i][j]=A[j][i]=v
    for i in range(N):
        if A[i][i]==X:
            if i+1<N and A[i][i+1]!=X:
                A[i][i]=A[i][i+1]
            elif i+1<N and A[i+1][i]!=X:
                A[i][i]=A[i+1][i]
    for i in range(len(A)):
        for j in range(len(A[0])):
            g2[ar1+i][ac1+j]=A[i][j]
    return g2