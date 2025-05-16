from collections import Counter
def solve(grid):
    h=len(grid); w=len(grid[0])
    def runs(row):
        rs=[]; cur=row[0]; cnt=1
        for x in row[1:]:
            if x==cur: cnt+=1
            else:
                rs.append((cur,cnt)); cur=x; cnt=1
        rs.append((cur,cnt)); return rs
    r0=runs(grid[0])
    widths=[cnt for _,cnt in r0]
    cntw=Counter(widths)
    shapeW=max([cw for cw,c in cntw.items() if c>1])
    starts=[]; acc=0
    for _,cnt in r0:
        if cnt==shapeW: starts.append(acc)
        acc+=cnt
    shapeH=0
    for r in range(h):
        if sum(1 for _,cnt in runs(grid[r]) if cnt==shapeW)>=2: shapeH+=1
        else: break
    maskH=shapeH-2; maskW=shapeW-2
    bg=grid[0][w-widths[-1]]
    bbs={}
    for y in range(h):
        for x in range(w):
            c=grid[y][x]
            if c not in bbs: bbs[c]=[y,y,x,x]
            else:
                bbs[c][0]=min(bbs[c][0],y); bbs[c][1]=max(bbs[c][1],y)
                bbs[c][2]=min(bbs[c][2],x); bbs[c][3]=max(bbs[c][3],x)
    masks=[]
    for c,(y0,y1,x0,x1) in bbs.items():
        if y1-y0+1==maskH and x1-x0+1==maskW:
            ok=True
            for yy in range(y0,y1+1):
                for xx in range(x0,x0+maskW):
                    v=grid[yy][xx]
                    if v!=c and v!=bg: ok=False; break
                if not ok: break
            if ok: masks.append((y0,x0,c))
    masks.sort()
    masks=[(y0,x0,c) for y0,x0,c in masks]
    mask_arrays=[]
    for y0,x0,c in masks:
        mask_arrays.append([grid[y][x0:x0+maskW] for y in range(y0,y0+maskH)])
    shapes=[]
    for st in starts:
        shapes.append([grid[r][st:st+shapeW] for r in range(shapeH)])
    res=[]
    for i,shape in enumerate(shapes):
        m=mask_arrays[i]
        s=[row[:] for row in shape]
        for dy in range(maskH):
            for dx in range(maskW):
                v=m[dy][dx]
                if v!=bg: s[dy+1][dx+1]=v
        res.append(s)
    out=[]
    for r in range(shapeH):
        row=[]
        for s in res: row+=s[r]
        out.append(row)
    return out