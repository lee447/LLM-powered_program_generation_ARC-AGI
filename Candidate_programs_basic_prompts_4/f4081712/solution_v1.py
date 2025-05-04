def solve(grid):
    H=len(grid); W=len(grid[0])
    border_colors=set(grid[0])
    bt=0
    for i in range(H):
        if set(grid[i]) - border_colors:
            break
        bt+=1
    bb=0
    for i in range(H-1,-1,-1):
        if set(grid[i]) - border_colors:
            break
        bb+=1
    border_side=border_colors|set(row[0] for row in grid)|set(row[-1] for row in grid)
    bl=0
    for j in range(W):
        if set(grid[i][j] for i in range(H)) - border_side:
            break
        bl+=1
    br=0
    for j in range(W-1,-1,-1):
        if set(grid[i][j] for i in range(H)) - border_side:
            break
        br+=1
    sub=[row[bl:W-br] for row in grid[bt:H-bb]]
    sh=len(sub); sw=len(sub[0])
    def good(h,w):
        for i in range(sh):
            for j in range(sw):
                if sub[i][j]!=sub[i%h][j%w]:
                    return False
        return True
    best=(sh,sw)
    for h in range(1,sh+1):
        if sh%h: continue
        for w in range(1,sw+1):
            if sw%w: continue
            if good(h,w) and h*w<best[0]*best[1]:
                best=(h,w)
    h,w=best
    return [row[:w] for row in sub[:h]]