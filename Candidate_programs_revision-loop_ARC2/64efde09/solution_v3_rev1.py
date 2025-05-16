import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = max({c: sum(row.count(c) for row in grid) for c in set(sum(grid, []))}, key=lambda x: sum(row.count(x) for row in grid))
    BORDER = 4
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    elbows = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]==BORDER:
                neigh = []
                for dr,dc in dirs:
                    rr,cc = r+dr,c+dc
                    if 0<=rr<h and 0<=cc<w and grid[rr][cc]!=bg and grid[rr][cc]!=BORDER:
                        neigh.append(((dr,dc),grid[rr][cc]))
                if len(neigh)==2 and abs(neigh[0][0][0]*neigh[1][0][0]+neigh[0][0][1]*neigh[1][0][1])==0:
                    elbows.append((r,c,neigh[0],neigh[1]))
    out = [row[:] for row in grid]
    def fill_h(r,c,dc,ch):
        if dc<0:
            for x in range(0,c):
                out[r][x] = ch
        else:
            for x in range(c+1,w):
                out[r][x] = ch
    def fill_v(r,c,dr,cv):
        if dr<0:
            for y in range(0,r):
                out[y][c] = cv
        else:
            for y in range(r+1,h):
                out[y][c] = cv
    midr, midc = h//2, w//2
    for r,c,n1,n2 in elbows:
        d1,col1 = n1; d2,col2 = n2
        mp = {d1:col1, d2:col2}
        # top-right: down and left
        if (1,0) in mp and (0,-1) in mp and r<midr and c>midc:
            fill_h(r,c,-1,mp[(0,-1)])
        # top-left: down and right
        if (1,0) in mp and (0,1) in mp and r<midr and c<midc:
            fill_h(r,c,1,mp[(0,1)])
        # bottom-right: up and left
        if (-1,0) in mp and (0,-1) in mp and r>midr and c>midc:
            fill_h(r,c,-1,mp[(0,-1)])
        # bottom-left: up and right
        if (-1,0) in mp and (0,1) in mp and r>midr and c<midc:
            fill_h(r,c,1,mp[(0,1)])
    for r,c,n1,n2 in elbows:
        d1,col1 = n1; d2,col2 = n2
        mp = {d1:col1, d2:col2}
        # top-right: down and left
        if (1,0) in mp and (0,-1) in mp and r<midr and c>midc:
            fill_v(r,c,1,mp[(1,0)])
        # top-left: down and right
        if (1,0) in mp and (0,1) in mp and r<midr and c<midc:
            fill_v(r,c,1,mp[(1,0)])
        # bottom-right: up and left
        if (-1,0) in mp and (0,-1) in mp and r>midr and c>midc:
            fill_v(r,c,-1,mp[(-1,0)])
        # bottom-left: up and right
        if (-1,0) in mp and (0,1) in mp and r>midr and c<midc:
            fill_v(r,c,-1,mp[(-1,0)])
    return out