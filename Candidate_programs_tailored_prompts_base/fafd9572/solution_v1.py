def solve(grid):
    h=len(grid); w=len(grid[0])
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not visited[i][j]:
                stack=[(i,j)]; comp=[]
                visited[i][j]=True
                while stack:
                    r,c=stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==1:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                comps.append(comp)
    comps.sort(key=lambda comp: (min(r for r,c in comp), min(c for r,c in comp)))
    anchors=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and grid[i][j]!=1:
                anchors.append((i,j,grid[i][j]))
    anchors.sort(key=lambda x:(x[0],x[1]))
    out=[row[:] for row in grid]
    for comp, anchor in zip(comps, anchors):
        color=anchor[2]
        for r,c in comp:
            out[r][c]=color
    return out