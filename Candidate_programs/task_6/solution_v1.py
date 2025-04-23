def solve(grid):
    n=len(grid)
    counts={}
    for i in range(n):
        for j in range(n):
            v=grid[i][j]
            if v!=0:
                counts[v]=counts.get(v,0)+1
    if not counts:
        return [[0]*(n*n) for _ in range(n*n)]
    mincount=min(counts.values())
    color=min(v for v,c in counts.items() if c==mincount)
    coords=[(i,j) for i in range(n) for j in range(n) if grid[i][j]==color]
    res=[[0]*(n*n) for _ in range(n*n)]
    for br,bc in coords:
        for i in range(n):
            for j in range(n):
                res[br*n+i][bc*n+j]=grid[i][j]
    return res