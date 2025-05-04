def solve(grid):
    H=len(grid);W=len(grid[0])
    comp_id=[[-1]*W for _ in range(H)]
    comps=[]
    for y in range(H):
        for x in range(W):
            if grid[y][x]!=0 and comp_id[y][x]==-1:
                cid=len(comps)
                cells=[]
                stack=[(x,y)]
                comp_id[y][x]=cid
                while stack:
                    cx,cy=stack.pop()
                    cells.append((cx,cy,grid[cy][cx]))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=cx+dx,cy+dy
                        if 0<=nx<W and 0<=ny<H and grid[ny][nx]!=0 and comp_id[ny][nx]==-1:
                            comp_id[ny][nx]=cid
                            stack.append((nx,ny))
                comps.append({'cells':cells})
    for c in comps:
        xs=[x for x,y,v in c['cells']]; ys=[y for x,y,v in c['cells']]
        c['min_x'],c['max_x']=min(xs),max(xs)
        c['min_y'],c['max_y']=min(ys),max(ys)
        c['width']=c['max_x']-c['min_x']+1
    row_groups={}
    for i,c in enumerate(comps):
        for x,y,v in c['cells']:
            row_groups.setdefault(y,set()).add(i)
    offsets=[0]*len(comps)
    for i,c in enumerate(comps):
        best_size=-1;best_r=None;best_off=0
        for r in sorted(r for x,y,v in c['cells'] for r in [y]):
            group=list(row_groups[r])
            size=len(group)
            group_width=sum(comps[j]['width'] for j in group)
            start=W-group_width
            order=sorted(group,key=lambda j:comps[j]['min_x'])
            off=0
            for j in order:
                if j==i:
                    off=start+off
                    break
                off+=comps[j]['width']
            if size>best_size or (size==best_size and (best_r is None or r<best_r)):
                best_size=size;best_r=r;best_off=off
        offsets[i]=best_off
    out=[[0]*W for _ in range(H)]
    for i,c in enumerate(comps):
        ox=offsets[i];bx=c['min_x']
        for x,y,v in c['cells']:
            out[y][ox+(x-bx)]=v
    return out