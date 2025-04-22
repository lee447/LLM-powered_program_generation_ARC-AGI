from collections import Counter
def solve(grid):
    h=len(grid); w=len(grid[0])
    cnt=Counter(v for row in grid for v in row)
    bg=cnt.most_common(1)[0][0]
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=bg and not visited[i][j]:
                col=grid[i][j]
                stack=[(i,j)]
                comp=[]
                mr=h
                visited[i][j]=True
                while stack:
                    r,c=stack.pop()
                    comp.append((r,c,col))
                    if r<mr: mr=r
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==col:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                comps.append((mr,comp))
    comps.sort(key=lambda x:x[0])
    out=[[bg]*w for _ in range(h)]
    for idx,(mr,comp) in enumerate(comps):
        shift = -1 if idx%2==0 else 1
        for r,c,v in comp:
            nc=c+shift
            if 0<=nc<w:
                out[r][nc]=v
    return out