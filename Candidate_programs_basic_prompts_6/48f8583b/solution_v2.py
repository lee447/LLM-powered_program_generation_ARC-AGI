def solve(grid):
    h=len(grid)
    w=len(grid[0])
    freq={}
    for i in range(h):
        for j in range(w):
            v=grid[i][j]
            freq[v]=freq.get(v,0)+1
    minc=min(freq.values())
    lows={v for v,c in freq.items() if c==minc}
    H=h*h
    W=w*w
    out=[[0]*W for _ in range(H)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] in lows:
                bi=i*h
                bj=j*w
                for di in range(h):
                    for dj in range(w):
                        out[bi+di][bj+dj]=grid[di][dj]
    return out