def solve(grid):
    H=len(grid); W=len(grid[0])
    cols=set()
    for y in range(H):
        for x in range(W):
            if grid[y][x]!=0:
                cols.add(grid[y][x])
    cols=sorted(cols, key=lambda c: min(x for y in range(H) for x in range(W) if grid[y][x]==c))
    left, right = cols[0], cols[1]
    def comps_of(c):
        vis=[[False]*W for _ in range(H)]
        comps=[]
        for y in range(H):
            for x in range(W):
                if grid[y][x]==c and not vis[y][x]:
                    stack=[(y,x)]; comp=[]
                    vis[y][x]=True
                    while stack:
                        yy,xx=stack.pop()
                        comp.append((yy,xx))
                        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                            y2, x2 = yy+dy, xx+dx
                            if 0<=y2<H and 0<=x2<W and not vis[y2][x2] and grid[y2][x2]==c:
                                vis[y2][x2]=True
                                stack.append((y2,x2))
                    comps.append(comp)
        return comps
    compsL=comps_of(left)
    compsR=comps_of(right)
    def shifts(comps):
        bs=[max(y for y,x in comp) for comp in comps]
        idx=sorted(range(len(comps)), key=lambda i: bs[i])
        i_hi,i_lo=idx[0],idx[1]
        b_lo=bs[i_lo]
        ymin_lo=min(y for y,x in comps[i_lo])
        ymax_lo=max(y for y,x in comps[i_lo])
        h_lo=ymax_lo-ymin_lo+1
        b_hi=bs[i_hi]
        shiftY=[0]*2
        shiftY[i_lo]=H-1-b_lo
        shiftY[i_hi]=H-1-b_hi-h_lo-1
        return shiftY, i_hi, i_lo
    shiftYL, hiL, loL = shifts(compsL)
    shiftYR, hiR, loR = shifts(compsR)
    # region widths
    def width_of(c,comps):
        return max(max(x for y,x in comp)-min(x for y,x in comp)+1 for comp in comps)
    WL=width_of(left, compsL)
    WR=width_of(right, compsR)
    startL=0
    startR=WL+1
    out=[[0]*W for _ in range(H)]
    for c, comps, shiftY, start in ((left, compsL, shiftYL, startL),(right, compsR, shiftYR, startR)):
        for i, comp in enumerate(comps):
            xmin=min(x for y,x in comp)
            dx = start - xmin
            dy = shiftY[i]
            for y,x in comp:
                out[y+dy][x+dx]=c
    return out