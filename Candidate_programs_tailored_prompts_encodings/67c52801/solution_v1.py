def solve(grid):
    R = len(grid)
    C = len(grid[0])
    border = grid[R-1][0]
    pillars = [c for c in range(C) if grid[R-2][c] == border]
    slots = []
    for i in range(len(pillars)-1):
        s = pillars[i]+1
        e = pillars[i+1]-1
        w = e-s+1
        if w>0:
            slots.append((s,e,w))
    visited = [[False]*C for _ in range(R)]
    clusters = []
    for r in range(R-2):
        for c in range(C):
            v = grid[r][c]
            if v!=0 and v!=border and not visited[r][c]:
                col = v
                stk = [(r,c)]
                coords = []
                visited[r][c] = True
                while stk:
                    x,y = stk.pop()
                    coords.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<R-2 and 0<=ny<C and not visited[nx][ny] and grid[nx][ny]==col:
                            visited[nx][ny]=True
                            stk.append((nx,ny))
                minr = min(x for x,y in coords)
                minc = min(y for x,y in coords)
                rel = [(x-minr,y-minc) for x,y in coords]
                h = max(x for x,y in rel)+1
                w = max(y for x,y in rel)+1
                variants = {}
                def add_variant(cells, H, W):
                    ww = max(y for x,y in cells)+1
                    if ww not in variants:
                        variants[ww] = (cells, H, W)
                add_variant(rel, h, w)
                # rot90
                rel90 = [(y, w-1-x) for x,y in rel]
                add_variant(rel90, w, h)
                # rot180
                rel180 = [(h-1-x, w-1-y) for x,y in rel]
                add_variant(rel180, h, w)
                # rot270
                rel270 = [(w-1-y, x) for x,y in rel]
                add_variant(rel270, w, h)
                clusters.append({"minc":minc,"color":col,"variants":variants})
    out = [row[:] for row in grid]
    for r in range(R-1):
        for c in range(C):
            if out[r][c]!=0 and out[r][c]!=border:
                out[r][c]=0
    used = [False]*len(clusters)
    for s,e,w in sorted(slots, key=lambda x: x[0]):
        candidates = [(i,clusters[i]["minc"]) for i in range(len(clusters)) if not used[i] and w in clusters[i]["variants"]]
        if not candidates: continue
        i,_ = min(candidates, key=lambda x: x[1])
        used[i]=True
        cells,H,W = clusters[i]["variants"][w]
        base_row = R-2
        for dx,dy in cells:
            rr = base_row - (H-1) + dx
            cc = s + dy
            out[rr][cc] = clusters[i]["color"]
    return out