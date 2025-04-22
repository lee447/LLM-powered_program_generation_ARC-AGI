def solve(grid):
    h=len(grid);w=len(grid[0])
    seen=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not seen[i][j]:
                val=grid[i][j]
                stack=[(i,j)];seen[i][j]=True;pts=[]
                while stack:
                    r,c=stack.pop()
                    pts.append((r,c))
                    for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc=r+dr,c+dc
                        if 0<=rr<h and 0<=cc<w and not seen[rr][cc] and grid[rr][cc]==val:
                            seen[rr][cc]=True
                            stack.append((rr,cc))
                comps.append((len(pts),val))
    comps.sort(key=lambda x:x[0],reverse=True)
    cluster=comps[-1][1]
    lines=comps[:-1]
    size=lines[0][0]
    frames=len(lines)
    out=[[0]*size for _ in range(size)]
    for i,(ln,val) in enumerate(lines):
        for j in range(i,size-i):
            out[i][j]=val;out[size-1-i][j]=val;out[j][i]=val;out[j][size-1-i]=val
    for r in range(frames,size-frames):
        for c in range(frames,size-frames):
            out[r][c]=cluster
    return out