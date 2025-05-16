import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = max({c: sum(row.count(c) for row in grid) for c in set(sum(grid, []))}, key=lambda x: sum(row.count(x) for row in grid))
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    pivots = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 4:
                neigh = []
                for dr,dc in dirs:
                    rr,cc = r+dr,c+dc
                    if 0<=rr<h and 0<=cc<w and grid[rr][cc]!=bg and grid[rr][cc]!=4:
                        neigh.append(((dr,dc),grid[rr][cc]))
                if len(neigh)==2 and abs(neigh[0][0][0]*neigh[1][0][0]+neigh[0][0][1]*neigh[1][0][1])==0:
                    pivots.append((r,c,neigh[0],neigh[1]))
    out = [row[:] for row in grid]
    init = grid
    for r,c,n1,n2 in pivots:
        for (dr,dc),col in (n1,n2):
            rr,cc = r+dr, c+dc
            while 0<=rr<h and 0<=cc<w and init[rr][cc] in (bg,col):
                if init[rr][cc]==bg:
                    out[rr][cc] = col
                rr += dr; cc += dc
    return out