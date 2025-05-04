def solve(grid):
    H=len(grid);W=len(grid[0])
    orig=[row[:] for row in grid]
    vis=[[False]*W for _ in range(H)]
    comps=[]
    for i in range(H):
        for j in range(W):
            if orig[i][j]==5 and not vis[i][j]:
                stack=[(i,j)];vis[i][j]=True;comp=[(i,j)]
                while stack:
                    r,c=stack.pop()
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=r+dr,c+dc
                        if 0<=rr<H and 0<=cc<W and not vis[rr][cc] and orig[rr][cc]==5:
                            vis[rr][cc]=True;stack.append((rr,cc));comp.append((rr,cc))
                comps.append(comp)
    for comp in comps:
        rs=[r for r,c in comp];cs=[c for r,c in comp]
        minr,maxr,minc,maxc=min(rs),max(rs),min(cs),max(cs)
        holes=[]
        for c in range(minc,maxc+1):
            if orig[minr][c]!=5:holes.append((minr,c))
            if orig[maxr][c]!=5:holes.append((maxr,c))
        for r in range(minr+1,maxr):
            if orig[r][minc]!=5:holes.append((r,minc))
            if orig[r][maxc]!=5:holes.append((r,maxc))
        if not holes:continue
        hr,hc=holes[0]
        if hr==minr:
            d1=(-1,0);side='top'
        elif hr==maxr:
            d1=(1,0);side='bottom'
        elif hc==minc:
            d1=(0,-1);side='left'
        else:
            d1=(0,1);side='right'
        for r in range(minr+1,maxr):
            for c in range(minc+1,maxc):
                if grid[r][c]!=5:grid[r][c]=2
        grid[hr][hc]=2
        r1, c1 = hr+d1[0], hc+d1[1]
        if 0<=r1<H and 0<=c1<W: grid[r1][c1]=2
        if side in ('top','bottom'):
            leftLen=0
            for c in range(hc-1,-1,-1):
                if orig[hr][c]==5: leftLen+=1
                else: break
            rightLen=0
            for c in range(hc+1,W):
                if orig[hr][c]==5: rightLen+=1
                else: break
            d2=(0,-1) if leftLen>rightLen else (0,1)
        else:
            upLen=0
            for r in range(hr-1,-1,-1):
                if orig[r][hc]==5: upLen+=1
                else: break
            downLen=0
            for r in range(hr+1,H):
                if orig[r][hc]==5: downLen+=1
                else: break
            d2=(-1,0) if upLen>downLen else (1,0)
        n=1
        while True:
            rr,cc=r1+d2[0]*n,c1+d2[1]*n
            if not (0<=rr<H and 0<=cc<W): break
            grid[rr][cc]=2
            n+=1
    return grid