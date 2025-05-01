def solve(grid):
    tile=[row[::-1] for row in grid[::-1]]
    h=[row[::-1] for row in tile]
    v=tile[::-1]
    b=[row[::-1] for row in v]
    out=[]
    for i in range(len(tile)):
        out.append(tile[i]+h[i])
    for i in range(len(tile)):
        out.append(v[i]+b[i])
    return out