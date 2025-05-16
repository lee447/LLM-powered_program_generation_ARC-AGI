from collections import Counter
def solve(grid):
    h=len(grid); w=len(grid[0])
    def runs_w(row):
        res=[]; cur=row[0]; cnt=1
        for x in row[1:]:
            if x==cur: cnt+=1
            else:
                res.append((cur,cnt)); cur=x; cnt=1
        res.append((cur,cnt)); return res
    r0=runs_w(grid[0])
    widths=[cnt for _,cnt in r0]
    cntw=Counter(widths)
    shapeW=max(k for k,v in cntw.items() if v>1)
    starts=[]; pos=0
    for c,cnt in r0:
        if cnt==shapeW: starts.append(pos)
        pos+=cnt
    shapeH=0
    for row in grid:
        if sum(1 for _,cnt in runs_w(row) if cnt==shapeW)>=2: shapeH+=1
        else: break
    maskH=shapeH-2; maskW=shapeW-2
    bg=next(c for c,cnt in r0 if cnt!=shapeW)
    shape_colors=[c for c,cnt in r0 if cnt==shapeW]
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
        if c!=bg and c not in shape_colors and y1-y0+1==maskH and x1-x0+1==maskW:
            masks.append((y0,x0))
    masks=sorted(masks)
    mask_arrays=[]
    for y0,x0 in masks:
        mask_arrays.append([grid[y][x0:x0+maskW] for y in range(y0,y0+maskH)])
    shapes=[]
    for st in starts:
        shapes.append([list(grid[r][st:st+shapeW]) for r in range(shapeH)])
    res=[]
    for shape,mask in zip(shapes,mask_arrays):
        for dy in range(maskH):
            for dx in range(maskW):
                v=mask[dy][dx]
                if v!=bg: shape[dy+1][dx+1]=v
        res.append(shape)
    out=[]
    for r in range(shapeH):
        row=[]
        for shape in res: row+=shape[r]
        out.append(row)
    return out