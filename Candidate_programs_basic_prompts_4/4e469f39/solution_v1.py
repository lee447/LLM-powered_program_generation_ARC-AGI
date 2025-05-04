def solve(grid):
    h, w = len(grid), len(grid[0])
    drs = [(-1,0),(1,0),(0,-1),(0,1)]
    gaps = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]==0:
                cnt = 0
                nbrs = []
                for dr,dc in drs:
                    rr, cc = r+dr, c+dc
                    if 0<=rr<h and 0<=cc<w and grid[rr][cc]==5:
                        cnt+=1
                        nbrs.append((dr,dc))
                if cnt==2 and abs(nbrs[0][0])!=abs(nbrs[1][0]):
                    gaps.append((r,c))
    out = [row[:] for row in grid]
    for idx,(r,c) in enumerate(gaps):
        out[r][c] = 2
        # extension row for top‐gaps
        re = r-1
        if re<0: continue
        # count zeros to left/right on extension row
        zl=zr=0
        for cc in range(c-1,-1,-1):
            if grid[re][cc]==0: zl+=1
            else: break
        for cc in range(c+1,w):
            if grid[re][cc]==0: zr+=1
            else: break
        if zl>zr:
            dc = -1
        elif zr>zl:
            dc = 1
        else:
            # if tie, look one row down from extension
            dl=dr=0
            for cc in range(c-1,-1,-1):
                if 0<=r< h and grid[r][cc]==5: dl+=1
                else: break
            for cc in range(c+1,w):
                if 0<=r< h and grid[r][cc]==5: dr+=1
                else: break
            dc = -1 if dl>=dr else 1
        cc = c
        while 0<=cc<w and out[re][cc]==0:
            out[re][cc] = 2
            cc += dc
    return out