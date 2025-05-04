def solve(grid):
    bg=grid[0][0]
    m=len(grid);n=len(grid[0])
    shapes=[]
    for color in {c for row in grid for c in row}:
        if color==bg: continue
        minr=m;maxr=-1;minc=n;maxc=-1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==color:
                    if i<minr: minr=i
                    if i>maxr: maxr=i
                    if j<minc: minc=j
                    if j>maxc: maxc=j
        h=maxr-minr+1; w=maxc-minc+1
        shapes.append((h*w,h,w,color))
    shapes.sort()
    H=max(s[1] for s in shapes); W=max(s[2] for s in shapes)
    out=[[None]*W for _ in range(H)]
    for _,h,w,color in shapes:
        for i in range(h):
            for j in range(w):
                if out[i][j] is None:
                    out[i][j]=color
    return out