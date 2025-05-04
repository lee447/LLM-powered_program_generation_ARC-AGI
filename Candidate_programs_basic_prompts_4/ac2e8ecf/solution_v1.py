def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] and not seen[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                seen[i][j] = True
                pts = []
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==col:
                            seen[nx][ny]=True
                            stack.append((nx,ny))
                rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                r0,r1,minr = min(rs),max(rs),min(rs)
                c0,c1,minc = min(cs),max(cs),min(cs)
                box = [[0]*(c1-c0+1) for _ in range(r1-r0+1)]
                for x,y in pts: box[x-r0][y-c0]=col
                comps.append((col,pts,box,r0,r1,c0,c1))
    rings,plus = [],[]
    for col,pts,box,_,_,_,_ in comps:
        rs = len(box); cs = len(box[0])
        if all(box[0][j] and box[rs-1][j] and box[j if rs==cs else 0][0] for j in range(cs)):
            rings.append((col,box))
        else:
            plus.append((col,box))
    rings.sort(key=lambda x: x[0])
    plus.sort(key=lambda x: x[0], reverse=True)
    out = [[0]*w for _ in range(h)]
    def pack(lst, top):
        y = 1 if top else h-1
        dir = 1 if top else -1
        x = 1
        for _,box in lst:
            bh, bw = len(box), len(box[0])
            yy = y if top else y-bh+1
            for i in range(bh):
                for j in range(bw):
                    if box[i][j]:
                        out[yy+i*dir][x+j] = box[i][j]
            x += bw+1
    pack(rings, True)
    pack(plus, False)
    return out