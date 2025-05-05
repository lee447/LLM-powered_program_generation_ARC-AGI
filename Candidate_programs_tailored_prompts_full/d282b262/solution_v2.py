def solve(grid):
    h=len(grid); w=len(grid[0])
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    vis=[[False]*w for _ in range(h)]
    cluster_map={}
    clusters=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=0 and not vis[r][c]:
                cells=[]; stack=[(r,c)]; vis[r][c]=True
                while stack:
                    y,x=stack.pop()
                    cells.append((y,x))
                    for dy,dx in dirs:
                        ny,nx=y+dy,x+dx
                        if 0<=ny<h and 0<=nx<w and grid[ny][nx]!=0 and not vis[ny][nx]:
                            vis[ny][nx]=True; stack.append((ny,nx))
                cid=len(clusters)
                for y,x in cells: cluster_map[(y,x)]=cid
                rows=[y for y,x in cells]
                clusters.append({'cells':cells,'minr':min(rows),'maxr':max(rows)})
    n=len(clusters)
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[rb]=ra
    for i in range(n):
        for j in range(i+1,n):
            if not (clusters[i]['maxr']<clusters[j]['minr'] or clusters[j]['maxr']<clusters[i]['minr']):
                union(i,j)
    groups={}
    for i in range(n):
        r=find(i)
        groups.setdefault(r,[]).append(i)
    shifts=[None]*n
    for grp in groups.values():
        cand_shifts={i:[] for i in grp}
        rows=set()
        for i in grp:
            rows.update(y for y,x in clusters[i]['cells'])
        for r in rows:
            segs=[]
            c=0
            while c<w:
                if grid[r][c]!=0 and cluster_map.get((r,c)) in grp:
                    cid=cluster_map[(r,c)]
                    vals=[]
                    start=c
                    while c<w and grid[r][c]!=0 and cluster_map.get((r,c))==cid:
                        vals.append(grid[r][c]); c+=1
                    segs.append((cid,start,len(vals),vals))
                else:
                    c+=1
            if not segs: continue
            total=sum(l for _,_,l,_ in segs)
            new_start=w-total
            offs=0
            for cid,start,l,vals in segs:
                shift=new_start+offs-start
                cand_shifts[cid].append(shift)
                offs+=l
        for cid in grp:
            shifts[cid]=min(cand_shifts[cid]) if cand_shifts[cid] else 0
    out=[[0]*w for _ in range(h)]
    for cid,cl in enumerate(clusters):
        s=shifts[cid]
        for y,x in cl['cells']:
            out[y][x+s]=grid[y][x]
    return out