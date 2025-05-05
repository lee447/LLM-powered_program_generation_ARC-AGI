from collections import deque
def solve(grid):
    R,C=len(grid),len(grid[0])
    out=[row[:] for row in grid]
    seen=[[False]*C for _ in range(R)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(R):
        for j in range(C):
            if grid[i][j]==6 and not seen[i][j]:
                q=deque([(i,j)]); seen[i][j]=True; pts=[(i,j)]
                while q:
                    r,c=q.popleft()
                    for dr,dc in dirs:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<R and 0<=nc<C and not seen[nr][nc] and grid[nr][nc]==6:
                            seen[nr][nc]=True; q.append((nr,nc)); pts.append((nr,nc))
                rs=[r for r,_ in pts]; cs=[c for _,c in pts]
                r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                for r in range(r0,r1+1):
                    for c in range(minc,maxc+1):
                        out[r][c]=7
                for r in range(r0,r1+1):
                    if minc-1>=0: out[r][minc-1]=grid[r][minc-1]
                    if maxc+1<C: out[r][maxc+1]=grid[r][maxc+1]
                for c in range(minc,maxc+1):
                    if r0-1>=0: out[r0-1][c]=grid[r0-1][c]
                    if r1+1<R: out[r1+1][c]=grid[r1+1][c]
    return out