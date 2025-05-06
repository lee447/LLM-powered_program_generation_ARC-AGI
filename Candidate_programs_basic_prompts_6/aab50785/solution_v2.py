def solve(grid):
    bands = {}
    for r in range(len(grid)-1):
        for c in range(len(grid[0])-1):
            if grid[r][c]==8 and grid[r][c+1]==8 and grid[r+1][c]==8 and grid[r+1][c+1]==8:
                bands.setdefault(r,[]).append(c)
    out=[]
    for r in sorted(bands):
        cs = sorted(bands[r])
        c1,c2 = cs[0],cs[1]
        for dr in (0,1):
            out.append(grid[r+dr][c1+2:c2])
    return out