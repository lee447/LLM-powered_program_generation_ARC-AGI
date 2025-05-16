def solve(grid):
    h=len(grid); w=len(grid[0])
    def runs(row):
        rs=[]; cur=row[0]; cnt=1
        for x in row[1:]:
            if x==cur: cnt+=1
            else:
                rs.append((cur,cnt)); cur=x; cnt=1
        rs.append((cur,cnt))
        return rs
    r0=runs(grid[0])
    widths=[cnt for _,cnt in r0]
    from collections import Counter
    cntw=Counter(widths)
    shapeW=max([cw for cw,cnt in cntw.items() if cnt>1])
    starts=[]; acc=0
    for colw in r0:
        if colw[1]==shapeW:
            starts.append(acc)
        acc+=colw[1]
    # stripes
    stripes=[]
    for r in range(h):
        rr=runs(grid[r])
        if sum(1 for _,cnt in rr if cnt==shapeW)>=2:
            if not stripes or stripes[-1]!=r:
                if r==0 or not(sum(1 for _,cnt in runs(grid[r-1]) if cnt==shapeW)>=2):
                    stripes.append(r)
    # shape heights
    sh=[]
    for sr in stripes:
        hh=0
        for r in range(sr,h):
            ok=True
            for st in starts:
                seg=grid[r][st:st+shapeW]
                if seg.count(seg[0])<shapeW-1:
                    ok=False; break
            if not ok: break
            hh+=1
        sh.append(hh)
    shapeH=sh[0]
    maskH=shapeH-2; maskW=shapeW-2
    # masks
    bbs={}
    for y in range(h):
        for x in range(w):
            c=grid[y][x]
            if c not in bbs: bbs[c]=[y,y,x,x]
            else:
                bbs[c][0]=min(bbs[c][0],y)
                bbs[c][1]=max(bbs[c][1],y)
                bbs[c][2]=min(bbs[c][2],x)
                bbs[c][3]=max(bbs[c][3],x)
    masks=[]
    for c,(y0,y1,x0,x1) in bbs.items():
        if y1-y0+1==maskH and x1-x0+1==maskW:
            ok=True
            for yy in range(y0,y1+1):
                for xx in range(x0,x1+1):
                    if grid[yy][xx]!=c and grid[yy][xx]!=grid[0][w-widths[-1]]:
                        ok=False; break
                if not ok: break
            if ok: masks.append((y0,x0,c))
    masks=sorted(masks)
    out=[]
    mlen=len(masks)
    mi=0
    for si,sr in enumerate(stripes):
        orows=shapeH if si==0 else maskH+1
        for dr in range(orows):
            row=[]
            for bi,st in enumerate(starts):
                base=grid[sr+dr][st:st+shapeW]
                if 1<=dr<shapeH-1:
                    y0,x0,c=masks[bi]
                    for dc in range(1,shapeW-1):
                        if grid[y0+dr-1][x0+dc-1]==c:
                            base[dc]=c
                row+=base
            out.append(row)
    return out