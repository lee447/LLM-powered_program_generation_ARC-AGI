from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    ans = [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not seen[i][j]:
                stack = [(i,j)]
                comp = []
                seen[i][j] = True
                minr,maxr,minc,maxc = i,i,j,j
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    if r<minr: minr=r
                    if r>maxr: maxr=r
                    if c<minc: minc=c
                    if c>maxc: maxc=c
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==1:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                ok = True
                for r,c in comp:
                    if not (r==minr or r==maxr or c==minc or c==maxc):
                        ok = False
                        break
                if ok:
                    for r,c in comp:
                        ans[r][c] = 2
    return ans