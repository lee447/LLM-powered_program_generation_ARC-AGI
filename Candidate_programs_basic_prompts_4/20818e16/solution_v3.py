def solve(grid):
    h,len0= len(grid),len(grid[0])
    freq={}
    for r in grid:
        for v in r:
            freq[v]=freq.get(v,0)+1
    bg=max(freq,key=lambda x:freq[x])
    shapes=[]
    for v in freq:
        if v==bg: continue
        minr,minc=h,len0
        maxr,maxc=0,0
        for i in range(h):
            for j in range(len0):
                if grid[i][j]==v:
                    if i<minr: minr=i
                    if i>maxr: maxr=i
                    if j<minc: minc=j
                    if j>maxc: maxc=j
        shapes.append((maxr-minr+1)*(maxc-minc+1, maxr-minr+1, maxc-minc+1, v))
    shapes.sort(reverse=True)
    _,H,W,c0=shapes[0]
    out=[[c0]*W for _ in range(H)]
    for _,h2,w2,c in shapes[1:]:
        for i in range(h2):
            for j in range(w2):
                out[i][j]=c
    return out