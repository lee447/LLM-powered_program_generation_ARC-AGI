def solve(grid):
    n = len(grid)
    coords = [(i,j) for i in range(n) for j in range(len(grid[i])) if grid[i][j] != 0]
    color = grid[coords[0][0]][coords[0][1]] if coords else 0
    m = n*2
    out = [[0]*m for _ in range(m)]
    offs = [(0,0),(0,n),(n,n),(n,0)]
    for r,c in coords:
        rots = [(r,c),(c,n-1-r),(n-1-r,n-1-c),(n-1-c,r)]
        for k,(rr,cc) in enumerate(rots):
            or0,oc0 = offs[k]
            out[or0+rr][oc0+cc] = color
    return out