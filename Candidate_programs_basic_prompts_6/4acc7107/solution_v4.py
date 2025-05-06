def solve(grid):
    H=len(grid); W=len(grid[0])
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    visited=[[False]*W for _ in range(H)]
    from collections import defaultdict, deque
    color_cells=defaultdict(list)
    for r in range(H):
        for c in range(W):
            v=grid[r][c]
            if v!=0:
                color_cells[v].append((r,c))
    # find clusters per color
    clusters_by_color={}
    for color, cells in color_cells.items():
        vset=set(cells)
        clusters=[]
        vis=set()
        for cell in cells:
            if cell in vis: continue
            q=[cell]; vis.add(cell)
            comp=[]
            for x,y in q:
                comp.append((x,y))
                for dr,dc in dirs:
                    nr, nc = x+dr, y+dc
                    if (nr,nc) in vset and (nr,nc) not in vis:
                        vis.add((nr,nc)); q.append((nr,nc))
            # bounding box and rel positions
            rs=[x for x,y in comp]; cs=[y for x,y in comp]
            r0=min(rs); c0=min(cs)
            rel=[(x-r0,y-c0) for x,y in comp]
            h=max(x for x,y in rel)+1; w=max(y for x,y in rel)+1
            clusters.append({"cells":rel,"h":h,"w":w,"size":len(rel)})
        # sort clusters by height ascending, tie by size ascending
        clusters.sort(key=lambda x:(x["h"],x["size"]))
        clusters_by_color[color]=(clusters[0],clusters[1])
    # sort colors by global min input col
    color_order=sorted(clusters_by_color.keys(), key=lambda c: min(y for x,y in color_cells[c]))
    # compute chunk widths and starts
    chunk_width={}
    for c in color_order:
        s,l=clusters_by_color[c]
        chunk_width[c]=max(s["w"],l["w"])
    chunk_start={}
    cur=0
    for c in color_order:
        chunk_start[c]=cur
        cur+=chunk_width[c]+1
    # place into result
    res=[[0]*W for _ in range(H)]
    gap=1
    for c in color_order:
        s,l=clusters_by_color[c]
        # vertical offset
        y0=H-(s["h"]+l["h"]+gap)
        # small cluster on top
        for dr,dc in s["cells"]:
            r=y0+dr; col=chunk_start[c]+dc
            res[r][col]=c
        y1=y0+s["h"]+gap
        for dr,dc in l["cells"]:
            r=y1+dr; col=chunk_start[c]+dc
            res[r][col]=c
    return res