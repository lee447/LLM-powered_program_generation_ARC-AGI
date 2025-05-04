def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [[0]*w for _ in range(h)]
    regions = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c and c!=1:
                if c not in regions:
                    regions[c] = [i,i,j,j]
                else:
                    regions[c][0] = min(regions[c][0], i)
                    regions[c][1] = max(regions[c][1], i)
                    regions[c][2] = min(regions[c][2], j)
                    regions[c][3] = max(regions[c][3], j)
    for c,(r0,r1,c0,c1) in regions.items():
        H = r1-r0+1
        W = c1-c0+1
        s = min(H,W)-1
        rr = r0
        cc = c0+(W-s)//2
        for i in range(rr, rr+s):
            for j in range(cc, cc+s):
                res[i][j] = c
    return res