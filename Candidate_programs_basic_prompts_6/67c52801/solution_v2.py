def solve(grid):
    h=len(grid); w=len(grid[0])
    base=grid[h-1][0]
    colors=set()
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            if c!=0 and c!=base:
                colors.add(c)
    shapes=[]
    for c in colors:
        minr,minc=h,w; maxr,maxc=-1,-1
        for i in range(h):
            for j in range(w):
                if grid[i][j]==c:
                    minr=min(minr,i); minc=min(minc,j)
                    maxr=max(maxr,i); maxc=max(maxc,j)
        sh=[] 
        for i in range(minr,maxr+1):
            row=[]
            for j in range(minc,maxc+1):
                row.append(grid[i][j] if grid[i][j]==c else 0)
            sh.append(row)
        for i in range(minr,maxr+1):
            for j in range(minc,maxc+1):
                if grid[i][j]==c:
                    grid[i][j]=0
        ph=len(sh); pw=len(sh[0])
        if ph==1 and pw>1:
            nsh=[[sh[0][j]] for j in range(pw)]
            sh=nsh; ph, pw = pw, 1
        shapes.append((ph*pw,c,sh,ph,pw))
    shapes.sort()
    segs=[]
    row=h-2
    j=0
    while j<w:
        if grid[row][j]==0:
            start=j
            while j<w and grid[row][j]==0:
                j+=1
            segs.append([start,j-start])
        else:
            j+=1
    for area,c,sh,ph,pw in shapes:
        for k,seg in enumerate(segs):
            if seg[1]>=pw:
                st=seg[0]
                for i in range(ph):
                    for j2 in range(pw):
                        if sh[i][j2]!=0:
                            grid[row-(ph-1)+i][st+j2]=sh[i][j2]
                if seg[1]==pw:
                    segs.pop(k)
                else:
                    seg[0]+=pw; seg[1]-=pw
                break
    return grid