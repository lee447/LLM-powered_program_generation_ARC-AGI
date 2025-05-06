def solve(grid):
    n=len(grid)
    m=len(grid[0]) if grid else 0
    dlen=min(n,m)
    pos=[i for i in range(dlen) if grid[i][i]!=0]
    if len(pos)<2: return grid
    pos.sort()
    step=pos[1]-pos[0]
    new_color=max(grid[i][i] for i in pos)+1
    i=pos[-1]+step
    while i<dlen:
        grid[i][i]=new_color
        i+=step
    return grid