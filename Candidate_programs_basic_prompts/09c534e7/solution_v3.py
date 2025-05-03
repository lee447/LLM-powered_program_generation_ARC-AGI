def solve(grid):
    m,len_row= len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*len_row for _ in range(m)]
    comps=[]
    for i in range(m):
        for j in range(len_row):
            if grid[i][j]!=0 and not visited[i][j]:
                stack=[(i,j)]
                pts=[]
                visited[i][j]=True
                while stack:
                    r,c=stack.pop()
                    pts.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<m and 0<=nc<len_row and grid[nr][nc]!=0 and not visited[nr][nc]:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                rs=[r for r,c in pts]; cs=[c for r,c in pts]
                r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                mask=tuple(tuple((r,c) in pts for c in range(minc,maxc+1)) for r in range(r0,r1+1))
                vals=[grid[r][c] for r,c in pts]
                from collections import Counter
                bg=Counter(vals).most_common(1)[0][0]
                cols=[(r-r0,c-minc,grid[r][c]) for r,c in pts if grid[r][c]!=bg]
                comps.append({"r0":r0,"c0":minc,"mask":mask,"cols":cols})
    patterns={}
    for idx,cmp in enumerate(comps):
        patterns.setdefault(cmp["mask"],[]).append(idx)
    for mask,idxs in patterns.items():
        rels={}
        for idx in idxs:
            for dr,dc,val in comps[idx]["cols"]:
                rels[(dr,dc)]=val
        if not rels: continue
        for idx in idxs:
            c=comps[idx]
            for (dr,dc),val in rels.items():
                out[c["r0"]+dr][c["c0"]+dc]=val
    return out