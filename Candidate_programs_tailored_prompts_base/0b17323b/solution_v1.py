def solve(grid):
    n=len(grid)
    m=len(grid[0]) if n>0 else 0
    limit=min(n,m)
    anchors=[i for i in range(limit) if grid[i][i]==1]
    anchors.sort()
    if len(anchors)<2:
        return grid
    step=anchors[1]-anchors[0]
    pos=anchors[-1]
    while pos+step<limit:
        pos+=step
        if grid[pos][pos]==0:
            grid[pos][pos]=2
    return grid