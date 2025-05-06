def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[row[:] for row in grid]
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not visited[i][j]:
                stack=[(i,j)]; visited[i][j]=True
                cells=[]
                while stack:
                    r,c=stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=r+dr,c+dc
                        if 0<=rr<h and 0<=cc<w and grid[rr][cc]==1 and not visited[rr][cc]:
                            visited[rr][cc]=True
                            stack.append((rr,cc))
                rs=[r for r,_ in cells]; cs=[c for _,c in cells]
                minr,maxr,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                comps.append((cells,minr,maxr,minc,maxc))
    hollow=[]; filled=[]
    for cells,minr,maxr,minc,maxc in comps:
        height=maxr-minr+1; width=maxc-minc+1
        cnt=len(cells)
        if cnt==height*width:
            filled.append((minr,maxr,minc,maxc))
        elif cnt==2*height+2*width-4:
            hollow.append((minr,maxr,minc,maxc))
        else:
            filled.append((minr,maxr,minc,maxc))
    for minr,maxr,minc,maxc in hollow:
        for r in range(minr+2,maxr-1):
            for c in range(minc+2,maxc-1):
                if 0<=r<h and 0<=c<w:
                    out[r][c]=6
        for r in (minr+1,maxr-1):
            if 0<=r<h:
                for c in range(minc+1,maxc):
                    if 0<=c<w:
                        out[r][c]=8
        for c in (minc+1,maxc-1):
            if 0<=c<w:
                for r in range(minr+1,maxr):
                    if 0<=r<h:
                        out[r][c]=8
    for minr,maxr,minc,maxc in filled+hollow:
        for r in range(minr-1,maxr+2):
            for c in range(minc-1,maxc+2):
                if 0<=r<h and 0<=c<w:
                    if r==minr-1 or r==maxr+1 or c==minc-1 or c==maxc+1 or r==minr or r==maxr or c==minc or c==maxc:
                        out[r][c]=2
    return out