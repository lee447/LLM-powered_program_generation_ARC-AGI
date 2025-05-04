def solve(grid):
    p=len(grid)
    freq={}
    for i in range(p):
        for j in range(p):
            freq[grid[i][j]]=freq.get(grid[i][j],0)+1
    m=min(freq.values())
    c=min(k for k,v in freq.items() if v==m)
    out=[[0]*(p*p) for _ in range(p*p)]
    for i in range(p):
        for j in range(p):
            if grid[i][j]==c:
                for di in range(p):
                    for dj in range(p):
                        out[i*p+di][j*p+dj]=grid[di][dj]
    return out