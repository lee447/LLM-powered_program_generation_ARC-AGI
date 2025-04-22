def solve(grid):
    H, W = len(grid), len(grid[0])
    cnt6 = [row.count(6) for row in grid]
    rows6 = {i for i,c in enumerate(cnt6) if c>0}
    cands = [(i,i+1,i+2) for i in range(H-2) if i in rows6 and i+1 in rows6 and i+2 in rows6]
    mid = (H-1)/2
    # pick top and middle bands
    low = min(cands, key=lambda t: (t[0]+t[1]+t[2])/3)
    midc = min(cands, key=lambda t: abs((t[0]+t[1]+t[2])/3-mid))
    bands = [low, midc]
    out = [row[:] for row in grid]
    for b in bands:
        m = {b[0]:1, b[1]:7, b[2]:9}
        for r in b:
            for c in range(W):
                if grid[r][c]==6:
                    out[r][c] = m[r]
    return out