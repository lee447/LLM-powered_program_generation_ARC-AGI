from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    seen = [[False]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]==1 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        rr,cc = r+dr,c+dc
                        if 0<=rr<H and 0<=cc<W and grid[rr][cc]==1 and not seen[rr][cc]:
                            seen[rr][cc] = True
                            stack.append((rr,cc))
                comps.append(comp)
    for comp in comps:
        rs = [r for r,_ in comp]; cs = [c for _,c in comp]
        r0,r1 = min(rs),max(rs); c0,c1 = min(cs),max(cs)
        full = True
        for r in range(r0,r1+1):
            for c in range(c0,c1+1):
                if grid[r][c]!=1:
                    full = False
                    break
            if not full: break
        if full:
            offs = [(1,2)]
        else:
            offs = [(0,2),(1,8),(2,6)]
        for offset,color in offs:
            rr0,rr1 = r0-offset,r1+offset
            cc0,cc1 = c0-offset,c1+offset
            for c in range(cc0,cc1+1):
                if 0<=rr0<H and 0<=c<W and out[rr0][c]==4: out[rr0][c]=color
                if 0<=rr1<H and 0<=c<W and out[rr1][c]==4: out[rr1][c]=color
            for r in range(rr0,rr1+1):
                if 0<=r<H and 0<=cc0<W and out[r][cc0]==4: out[r][cc0]=color
                if 0<=r<H and 0<=cc1<W and out[r][cc1]==4: out[r][cc1]=color
    return out