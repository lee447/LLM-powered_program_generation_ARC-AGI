def solve(grid):
    R, C = len(grid), len(grid[0])
    color = None
    for row in grid:
        for v in row:
            if v != 0:
                color = v
                break
        if color is not None:
            break
    H = [r for r in range(R) if any(c and grid[r][c]==color and grid[r][c+1]==color for c in range(C-1))]
    V = [c for c in range(C) if any(r and grid[r][c]==color and grid[r-1][c]==color for r in range(1,R))]
    Hs = {r:i for i,r in enumerate(H)}
    Vs = {c:i for i,c in enumerate(V)}
    out = [[0]*C for _ in range(R)]
    def ph(k):
        return (1 if k%2==1 else 0)
    def pv(j):
        m = j%4
        return -1 if m==0 else (1 if m==2 else 0)
    for r in range(R):
        for c in range(C):
            if grid[r][c]==color:
                h = (c>0 and grid[r][c-1]==color) or (c+1<C and grid[r][c+1]==color)
                if h and r in Hs:
                    k = Hs[r]
                    dc = ph(k)
                else:
                    if c in Vs:
                        i = sum(1 for hh in H if hh<r)-1
                        j = r - H[i] - 1
                        dc = pv(j)
                    else:
                        continue
                out[r][c+dc] = color
    return out