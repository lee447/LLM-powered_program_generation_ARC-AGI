def solve(grid):
    H=len(grid); W=len(grid[0]) if H>0 else 0
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    blues={(r,c) for r in range(H) for c in range(W) if grid[r][c]==1}
    visited=set()
    comps=[]
    for cell in blues:
        if cell in visited: continue
        stack=[cell]; comp=[]
        while stack:
            r,c=stack.pop()
            if (r,c) in visited: continue
            visited.add((r,c)); comp.append((r,c))
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr,nc) in blues and (nr,nc) not in visited:
                    stack.append((nr,nc))
        comps.append(comp)
    res=[row[:] for row in grid]
    if len(comps)>3:
        from collections import Counter
        cnt=Counter()
        for r in range(H):
            for c in range(W):
                v=grid[r][c]
                if v!=0 and v!=1: cnt[v]+=1
        hues=sorted(cnt.keys(), key=lambda x:cnt[x])
        h1,h2=hues[0],hues[1]
        for comp in comps:
            sr=sum(r for r,c in comp)/len(comp)
            sc=sum(c for r,c in comp)/len(comp)
            hue = h1 if abs(sr-sc)<1 else h2
            for r,c in comp: res[r][c]=hue
    else:
        anchors=[(r,c,grid[r][c]) for r in range(H) for c in range(W) if grid[r][c]!=0 and grid[r][c]!=1]
        minr=min(a[0] for a in anchors)
        maxr=max(a[0] for a in anchors)
        rowmin=[a for a in anchors if a[0]==minr]
        UL_anchor=min(rowmin, key=lambda x:x[1])
        UR_anchor=max(rowmin, key=lambda x:x[1])
        lowrow=[a for a in anchors if a[0]==maxr]
        LL_anchor=min(lowrow, key=lambda x:x[1])
        a_UL=a_UR=a_LL=None
        for comp in comps:
            sr=sum(r for r,c in comp)/len(comp)
            sc=sum(c for r,c in comp)/len(comp)
            if sr==min([sum(r for r,c in cp)/len(cp) for cp in comps]):
                if sc==min([sum(c for r,c in cp)/len(cp) for cp in comps if sum(r for r,c in cp)/len(cp)==sr]):
                    a_UL=(comp,UL_anchor[2])
                else:
                    a_UR=(comp,UR_anchor[2])
            else:
                a_LL=(comp,LL_anchor[2])
        for comp,hue in (a_UL,a_UR,a_LL):
            for r,c in comp: res[r][c]=hue
    return res