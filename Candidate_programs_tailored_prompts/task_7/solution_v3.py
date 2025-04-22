def solve(grid):
    H=len(grid);W=len(grid[0])
    visited=[[False]*W for _ in range(H)]
    clusters_by_color={}
    for i in range(H):
        for j in range(W):
            c=grid[i][j]
            if c!=0 and not visited[i][j]:
                stack=[(i,j)];comp=[]
                visited[i][j]=True
                while stack:
                    r,c0=stack.pop()
                    comp.append((r,c0))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=r+dr,c0+dc
                        if 0<=rr<H and 0<=cc<W and not visited[rr][cc] and grid[rr][cc]==grid[r][c0]:
                            visited[rr][cc]=True
                            stack.append((rr,cc))
                clusters_by_color.setdefault(grid[i][j],[]).append(comp)
    info={}
    for c,comps in clusters_by_color.items():
        comps_sorted=sorted(comps, key=lambda comp: len(comp))
        sc,lc=comps_sorted[0],comps_sorted[1]
        def mk(comp):
            rs=[r for r,_ in comp];cs=[c0 for _,c0 in comp]
            r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
            return {"cells":comp,"minr":r0,"minc":minc,"h":r1-r0+1,"w":max(cs)-minc+1}
        info[c]={"small":mk(sc),"large":mk(lc)}
    colors=sorted(info.keys(), key=lambda c: len(info[c]["small"]["cells"]))
    left,right=colors
    lw=max(info[left]["small"]["w"],info[left]["large"]["w"])
    co_left=0;co_right=lw+1
    out=[[0]*W for _ in range(H)]
    for color,co in ((left,co_left),(right,co_right)):
        sc=info[color]["small"];lc=info[color]["large"]
        lb=H-lc["h"];sb=lb-1-sc["h"]
        for r,c0 in sc["cells"]:
            dr,dc=r-sc["minr"],c0-sc["minc"]
            out[sb+dr][co+dc]=color
        for r,c0 in lc["cells"]:
            dr,dc=r-lc["minr"],c0-lc["minc"]
            out[lb+dr][co+dc]=color
    return out