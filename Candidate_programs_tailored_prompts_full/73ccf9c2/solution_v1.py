def solve(grid):
    R=len(grid); C=len(grid[0])
    visited=[[False]*C for _ in range(R)]
    comps=[]
    for i in range(R):
        for j in range(C):
            if grid[i][j]!=0 and not visited[i][j]:
                col=grid[i][j]
                stack=[(i,j)]
                visited[i][j]=True
                comp=[]
                while stack:
                    r,c=stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=r+dr,c+dc
                        if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==col:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                comps.append(comp)
    msize=max(len(comp) for comp in comps)
    comps=[comp for comp in comps if len(comp)==msize]
    comps.sort(key=lambda comp:(min(r for r,c in comp),min(c for r,c in comp)))
    comp=comps[0]
    minr=min(r for r,c in comp); maxr=max(r for r,c in comp)
    minc=min(c for r,c in comp); maxc=max(c for r,c in comp)
    H=maxr-minr+1; W=maxc-minc+1
    out=[[0]*W for _ in range(H)]
    for r,c in comp:
        out[r-minr][c-minc]=grid[r][c]
    return out