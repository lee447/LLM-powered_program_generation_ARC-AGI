from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    nrows, ncols = len(grid), len(grid[0])
    colors = set(c for row in grid for c in row)
    # find stripe color and its bounding box
    def find_comps(c):
        seen = [[False]*ncols for _ in range(nrows)]
        comps = []
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == c and not seen[i][j]:
                    q = deque([(i,j)])
                    seen[i][j] = True
                    comp = []
                    while q:
                        r,c0 = q.popleft()
                        comp.append((r,c0))
                        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                            rr,cc = r+dr, c0+dc
                            if 0<=rr<nrows and 0<=cc<ncols and not seen[rr][cc] and grid[rr][cc]==c:
                                seen[rr][cc]=True
                                q.append((rr,cc))
                    comps.append(comp)
        return comps

    stripe_c = None
    R0=R1=C0=C1=0
    for c in colors:
        comps = find_comps(c)
        if len(comps)==1:
            comp = comps[0]
            minr = min(r for r,_ in comp)
            maxr = max(r for r,_ in comp)
            minc = min(c0 for _,c0 in comp)
            maxc = max(c0 for _,c0 in comp)
            if (maxr-minr+1)*(maxc-minc+1)==len(comp) and len(comp)>1:
                stripe_c = c
                R0,R1,C0,C1 = minr,maxr,minc,maxc
                break
    # find vertical period pr
    def ok_pr(pr):
        for i in range(nrows-pr):
            if i<=R1 and i+pr>=R0: continue
            for j in range(ncols):
                if grid[i][j]==stripe_c: continue
                if grid[i+pr][j]==stripe_c: continue
                if grid[i][j]!=grid[i+pr][j]:
                    return False
        return True
    pr = 1
    while pr < nrows:
        if ok_pr(pr): break
        pr += 1
    # find horizontal period pc
    def ok_pc(pc):
        for j in range(ncols-pc):
            if j<=C1 and j+pc>=C0: continue
            for i in range(nrows):
                if grid[i][j]==stripe_c: continue
                if grid[i][j+pc]==stripe_c: continue
                if grid[i][j]!=grid[i][j+pc]:
                    return False
        return True
    pc = 1
    while pc < ncols:
        if ok_pc(pc): break
        pc += 1
    # collect candidate blocks
    center_r, center_c = nrows/2, ncols/2
    best = None
    bd = 1e9
    for i in range(nrows-pr+1):
        for j in range(ncols-pc+1):
            ok = True
            for r in range(i, i+pr):
                for c0 in range(j, j+pc):
                    if grid[r][c0] == stripe_c:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            cr = i + pr/2
            cc = j + pc/2
            d = abs(cr-center_r) + abs(cc-center_c)
            if d < bd:
                bd = d
                best = (i,j)
    i0,j0 = best
    return [row[j0:j0+pc] for row in grid[i0:i0+pr]]