def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[row[:] for row in grid]
    visited=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not visited[i][j]:
                stack=[(i,j)]
                visited[i][j]=True
                cells=[]
                minr,maxr,minc,maxc=i,i,j,j
                while stack:
                    r,c=stack.pop()
                    cells.append((r,c))
                    if r<minr: minr=r
                    if r>maxr: maxr=r
                    if c<minc: minc=c
                    if c>maxc: maxc=c
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=r+dr,c+dc
                        if 0<=rr<h and 0<=cc<w and not visited[rr][cc] and grid[rr][cc]==8:
                            visited[rr][cc]=True
                            stack.append((rr,cc))
                for r in range(minr,maxr+1):
                    for c in range(minc,maxc+1):
                        if (r==minr or r==maxr or c==minc or c==maxc) and grid[r][c]==0:
                            out[r][c]=2
    return out