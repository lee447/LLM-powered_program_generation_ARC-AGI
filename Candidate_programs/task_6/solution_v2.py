def solve(grid):
    R=len(grid); C=len(grid[0])
    counts={}
    for i in range(R):
        for j in range(C):
            v=grid[i][j]
            if v!=0:
                counts[v]=counts.get(v,0)+1
    min_count=min(counts.values())
    min_color=next(v for v,c in counts.items() if c==min_count)
    positions=[(i,j) for i in range(R) for j in range(C) if grid[i][j]==min_color]
    out=[[0]*(C*C) for _ in range(R*R)]
    for bi,bj in positions:
        off_i=bi*R; off_j=bj*C
        for i in range(R):
            for j in range(C):
                out[off_i+i][off_j+j]=grid[i][j]
    return out