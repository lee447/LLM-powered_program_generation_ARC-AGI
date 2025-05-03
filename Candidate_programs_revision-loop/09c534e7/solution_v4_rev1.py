from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not vis[i][j]:
                stack=[(i,j)]
                comp=[]
                vis[i][j]=True
                while stack:
                    r,c=stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]==1 and not vis[nr][nc]:
                            vis[nr][nc]=True
                            stack.append((nr,nc))
                # find any marker inside bounding box
                minr=min(r for r,c in comp)
                maxr=max(r for r,c in comp)
                minc=min(c for r,c in comp)
                maxc=max(c for r,c in comp)
                color=None
                for r in range(minr+1, maxr):
                    for c in range(minc+1, maxc):
                        if grid[r][c]>1:
                            color=grid[r][c]
                if color is None:
                    continue
                # fill every 1 in comp that lies strictly inside the comp's bounding box of zeros‐cuts
                for r,c in comp:
                    if minr<r<maxr and minc<c<maxc:
                        out[r][c]=color
    return out