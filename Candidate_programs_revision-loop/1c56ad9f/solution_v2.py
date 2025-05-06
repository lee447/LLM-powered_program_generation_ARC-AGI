def solve(grid):
    H, W = len(grid), len(grid[0])
    out = [[0]*W for _ in range(H)]
    color = None
    for r in range(H):
        for c in range(W):
            if grid[r][c]!=0:
                color = grid[r][c]
                break
        if color is not None: break
    rows = [r for r in range(H) if any(grid[r][c]==color for c in range(W)) and sum(grid[r][c]==color for c in range(W))>1]
    if not rows: return grid
    hs = sorted(rows)
    vs = sorted({c for r in range(H) for c in range(W) if grid[r][c]==color and ((r-1>=0 and grid[r-1][c]==color) or (r+1<H and grid[r+1][c]==color))})
    for r in range(H):
        for c in range(W):
            if grid[r][c]==color:
                if any(0<=c+dc<W and grid[r][c+dc]==color for dc in (-1,1)):
                    out[r][c] = color
    regions = []
    for i in range(len(hs)-1):
        a, b = hs[i], hs[i+1]
        if b>a+1:
            regions.append((a,b))
    for idx,(a,b) in enumerate(regions):
        height = b-a-1
        if height<=0: continue
        if len(regions)==1 or idx*2<len(regions)*1:
            cycle = [-1,0,1,0]
        else:
            cycle = [0,-1,0,1]
        for d in range(1,height+1):
            r = a+d
            off = cycle[(d-1)%4]
            for c in vs:
                if grid[r][c]==color:
                    nc = c+off
                    if 0<=nc<W:
                        out[r][nc] = color
    return out