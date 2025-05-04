def solve(grid):
    H=len(grid); W=len(grid[0])
    pos={}
    for r in range(H):
        for c in range(W):
            v=grid[r][c]
            if v not in pos: pos[v]=[r,r,c,c,0]
            p=pos[v]
            p[0]=min(p[0],r); p[1]=max(p[1],r)
            p[2]=min(p[2],c); p[3]=max(p[3],c)
            p[4]+=1
    mask_val=None
    for v,(r0,r1,c0,c1,cnt) in pos.items():
        h=r1-r0+1; w=c1-c0+1
        if cnt==h*w and h>1 and w>1:
            if mask_val is None or h*w> (pos[mask_val][1]-pos[mask_val][0]+1)*(pos[mask_val][3]-pos[mask_val][2]+1):
                mask_val=v
    if mask_val is None:
        return []
    r0,r1,c0,c1,_=pos[mask_val]
    h=r1-r0+1; w=c1-c0+1
    freq={}
    best=None; bestc=-1
    for r in range(H-h+1):
        for c in range(W-w+1):
            if not (r+h-1<r0 or r>r1 or c+w-1<c0 or c>c1):
                continue
            ok=True
            block=[]
            for i in range(h):
                row=grid[r+i]
                br=[]
                for j in range(w):
                    if row[c+j]==mask_val:
                        ok=False; break
                    br.append(row[c+j])
                if not ok: break
                block.append(tuple(br))
            if not ok: continue
            key=tuple(block)
            freq[key]=freq.get(key,0)+1
            if freq[key]>bestc:
                bestc=freq[key]; best=key
    return [list(row) for row in best]