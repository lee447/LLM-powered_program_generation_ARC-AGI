def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False]*W for _ in range(H)]
    clusters = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v and not visited[r][c]:
                pts = [(r,c)]
                visited[r][c] = True
                q = [(r,c)]
                while q:
                    x,y = q.pop()
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==v:
                            visited[nx][ny] = True
                            pts.append((nx,ny))
                            q.append((nx,ny))
                clusters.setdefault(v,[]).append(pts)
    def bbox(pts):
        rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
        return min(rs),min(cs),max(rs),max(cs)
    def choose(pts_list):
        info=[]
        for pts in pts_list:
            r0,c0,r1,c1 = bbox(pts)
            h,w = r1-r0+1,c1-c0+1
            diff=abs(h-w)
            fill = len(pts)/(h*w)
            top = r0
            info.append((diff,-fill,top,pts,r0,c0,h,w))
        info.sort(key=lambda x:(x[0],x[1],x[2]))
        sq = info[0]
        el = info[1]
        return sq[3],sq[4],sq[5],sq[6],el[3],el[4],el[5],el[6]
    color_info = []
    for v,cls in clusters.items():
        sq, r0s,c0s,hs,ws, el, r0e,c0e,he,we = choose(cls)
        color_info.append((v, sq, r0s,c0s,hs,ws, el, r0e,c0e,he,we))
    # sort by input square min_col
    color_info.sort(key=lambda x: x[3])
    start1 = H//2
    res = [[0]*W for _ in range(H)]
    for i,(v, sq, r0s,c0s,hs,ws, el, r0e,c0e,he,we) in enumerate(color_info):
        offc = 0 if i==0 else W-ws
        for r,c in sq:
            nr = (r-r0s)+start1
            nc = (c-c0s)+offc
            res[nr][nc] = v
        start2 = start1+hs+1
        offc2 = 0 if i==0 else W-we
        for r,c in el:
            nr = (r-r0e)+start2
            nc = (c-c0e)+offc2
            res[nr][nc] = v
    return res