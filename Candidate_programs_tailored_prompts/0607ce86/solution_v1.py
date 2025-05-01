def solve(grid):
    H, W = len(grid), len(grid[0])
    def find_anchors():
        anchors=[]
        for r in range(H):
            runs=[]
            c=0
            while c<W:
                v=grid[r][c]
                if v!=0:
                    j=c
                    while j<W and grid[r][j]==v: j+=1
                    runs.append((v,j-c))
                    c=j
                else:
                    c+=1
            for v,l in runs:
                if l>=W//4:
                    anchors.append(r)
                    break
        return sorted(set(anchors))
    def flood(r,c,seen):
        col=grid[r][c]
        stack=[(r,c)]
        comp=[]
        while stack:
            i,j=stack.pop()
            if (i,j) in seen: continue
            seen.add((i,j))
            comp.append((i,j))
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i+di, j+dj
                if 0<=ni<H and 0<=nj<W and grid[ni][nj]==col:
                    stack.append((ni,nj))
        return comp
    anchors = find_anchors()
    segments = []
    prev = -1
    for a in anchors:
        segments.append((prev+1,a-1))
        prev=a
    segments.append((prev+1,H-1))
    out = [[0]*W for _ in range(H)]
    for (r0,r1) in segments:
        if r0>r1: continue
        seen=set()
        comps=[]
        for r in range(r0,r1+1):
            for c in range(W):
                if grid[r][c]!=0 and r not in anchors and (r,c) not in seen:
                    comp=flood(r,c,seen)
                    if len(comp)>1:
                        rs=[p[0] for p in comp]
                        cs=[p[1] for p in comp]
                        comps.append((min(rs),max(rs),min(cs),max(cs)))
        if not comps: continue
        heights=[b-a+1 for a,b,_,_ in comps]
        from collections import Counter
        h = Counter(heights).most_common(1)[0][0]
        top = min(a for a,_,_,_ in comps if b-a+1==h)
        for r in range(top,top+h):
            for c in range(W):
                if grid[r][c]!=0 and r not in anchors:
                    out[r][c]=grid[r][c]
    return out