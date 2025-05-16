def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = max({c:0 for row in grid for c in row}, key=lambda c: sum(row.count(c) for row in grid))
    pts = [(y,x,grid[y][x]) for y in range(h) for x in range(w) if grid[y][x]!=bg and grid[y][x]!=4]
    xs = sorted({x for y,x,_ in pts})
    ys = sorted({y for y,x,_ in pts})
    cx0 = min(x for y,x,c in pts if all(grid[yy][x]==4 or yy<0 for yy in range(h)))
    cy0 = min(y for y,x,c in pts if all(grid[y][xx]==4 or xx<0 for xx in range(w)))
    out = [row[:] for row in grid]
    for y,x,c in pts:
        if x<cx0:
            if all(grid[y][xx] in (c,4) for xx in range(x,x+1)):
                for xx in range(0,cx0):
                    out[y][xx]=c
        if y>cy0:
            if all(grid[yy][x] in (c,4) for yy in range(y,y+1)):
                for yy in range(cy0,h):
                    out[yy][x]=c
    return out