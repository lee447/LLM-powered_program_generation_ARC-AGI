def solve(grid):
    h=len(grid); w=len(grid[0])
    freq={}
    for row in grid:
        for v in row:
            freq[v]=freq.get(v,0)+1
    bg=max(freq.items(), key=lambda x:x[1])[0]
    rects=[]
    for c,count in freq.items():
        if c==bg: continue
        minr, maxr = h, -1
        minc, maxc = w, -1
        for i in range(h):
            for j in range(w):
                if grid[i][j]==c:
                    if i<minr: minr=i
                    if i>maxr: maxr=i
                    if j<minc: minc=j
                    if j>maxc: maxc=j
        ph=maxr-minr+1; pw=maxc-minc+1
        rects.append((ph*pw, ph, pw, c))
    rects.sort(reverse=True, key=lambda x:x[0])
    _, H, W, color0 = rects[0]
    out=[[color0]*W for _ in range(H)]
    for _, ph, pw, c in rects[1:]:
        for i in range(ph):
            for j in range(pw):
                out[i][j]=c
    return out