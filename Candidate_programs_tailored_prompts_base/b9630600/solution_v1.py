def solve(grid):
    h=len(grid);w=len(grid[0])
    seen=[[False]*w for _ in range(h)]
    rects=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not seen[i][j]:
                stack=[(i,j)]
                seen[i][j]=True
                cells=[]
                while stack:
                    r,c=stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]==3 and not seen[nr][nc]:
                            seen[nr][nc]=True
                            stack.append((nr,nc))
                rs=[r for r,c in cells]; cs=[c for r,c in cells]
                minr,maxr,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                midr=(minr+maxr)//2; midc=(minc+maxc)//2
                rects.append((midr,midc))
    center_r=h//2; center_c=w//2
    quad={}
    for midr,midc in rects:
        qy=0 if midr<center_r else 1
        qx=0 if midc<center_c else 1
        quad[(qx,qy)]=(midr,midc)
    out=[row[:] for row in grid]
    for qy in (0,1):
        if (0,qy) in quad and (1,qy) in quad:
            r=quad[(0,qy)][0]
            c1=quad[(0,qy)][1]; c2=quad[(1,qy)][1]
            for c in range(min(c1,c2),max(c1,c2)+1):
                out[r][c]=3
    for qx in (0,1):
        if (qx,0) in quad and (qx,1) in quad:
            c=quad[(qx,0)][1]
            r1=quad[(qx,0)][0]; r2=quad[(qx,1)][0]
            for r in range(min(r1,r2),max(r1,r2)+1):
                out[r][c]=3
    return out