def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [[0]*w for _ in range(h)]
    for i,row in enumerate(grid):
        vals = [x for x in row if x!=0]
        start = w - len(vals)
        for j,v in enumerate(vals):
            out[i][start+j] = v
    return out