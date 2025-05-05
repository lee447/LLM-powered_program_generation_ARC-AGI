def solve(grid):
    H=len(grid); W=len(grid[0])
    anchors=[c for c in range(W) if grid[0][c]!=0]
    palette=[grid[0][c] for c in anchors]
    visited=[[False]*W for _ in range(H)]
    comps=[]
    for r in range(H):
        for c in range(W):
            if grid[r][c]==8 and not visited[r][c]:
                stack=[(r,c)]; visited[r][c]=True
                cells=[]
                while stack:
                    x,y=stack.pop()
                    cells.append((x,y))
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==8:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                rs=[x for x,_ in cells]; cs=[y for _,y in cells]
                comps.append((min(rs),max(rs),min(cs),max(cs),cells))
    minr=min(c[0] for c in comps); maxr=max(c[1] for c in comps)
    topl=[c for c in comps if c[0]==minr]
    botl=[c for c in comps if c[1]==maxr]
    topl=sorted(topl,key=lambda x:x[2])
    botl=sorted(botl,key=lambda x:x[2])
    tops=[c[3]-c[2]+1 for c in topl]
    bots=[c[3]-c[2]+1 for c in botl]
    K=len(palette)
    widths=[]
    ti=0; bi=0; pick=True
    while len(widths)<K:
        if pick:
            if ti<len(tops):
                widths.append(tops[ti]); ti+=1
            else:
                widths.append(bots[min(bi,len(bots)-1)]); bi+=1
        else:
            if bi<len(bots):
                widths.append(bots[bi]); bi+=1
            else:
                widths.append(tops[min(ti,len(tops)-1)]); ti+=1
        pick=not pick
    minc=min(c[2] for c in comps); maxc=max(c[3] for c in comps)
    segs=[]
    x=minc
    for i,w in enumerate(widths):
        if i==K-1:
            segs.append((x,maxc))
        else:
            segs.append((x,x+w-1))
            x+=w
    out=[[0]*W for _ in range(H)]
    for _,_,c0,c1,cells in comps:
        for r,c in cells:
            for i,(s,e) in enumerate(segs):
                if s<=c<=e:
                    out[r][c]=palette[i]
                    break
    return out