from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            c = grid[i][j]
            if c!=0 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j]=True
                cells=[]
                while stack:
                    x,y=stack.pop()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                minr=min(x for x,y in cells)
                maxr=max(x for x,y in cells)
                minc=min(y for x,y in cells)
                maxc=max(y for x,y in cells)
                h=maxr-minr+1
                w=maxc-minc+1
                mask=[[0]*w for _ in range(h)]
                for x,y in cells:
                    mask[x-minr][y-minc]=c
                comps.append((mask,h*w,minr,minc,c))
    best=None
    for mask,area,minr,minc,c in comps:
        h=len(mask); w=len(mask[0])
        ok=True
        for r in range(h):
            for x in range(w):
                if mask[r][x]!=mask[r][w-1-x]:
                    ok=False; break
            if not ok: break
        if ok:
            if best is None or area>best[0]:
                best=(area,mask)
    return best[1]