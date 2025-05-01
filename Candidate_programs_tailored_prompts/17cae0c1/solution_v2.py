def solve(grid):
    h=len(grid)
    w=len(grid[0])
    zone_w=w//3
    zones=[[(r,c) for r in range(h) for c in range(i*zone_w,(i+1)*zone_w)] for i in range(3)]
    colors=[]
    nxt=1
    for z in zones:
        while nxt in (0,5): nxt+=1
        colors.append(nxt)
        nxt+=1
    out=[[0]*w for _ in range(h)]
    for i,z in enumerate(zones):
        for r,c in z:
            out[r][c]=colors[i]
    return out