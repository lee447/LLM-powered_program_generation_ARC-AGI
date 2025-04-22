def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    comps = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v and not seen[r][c]:
                color = v
                stack = [(r,c)]
                comp = []
                seen[r][c] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==color:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                comps.setdefault(color, []).append(comp)
    infos = []
    for color, lst in comps.items():
        info = []
        for comp in lst:
            rs = [p[0] for p in comp]
            cs = [p[1] for p in comp]
            r0,r1,minc,maxc = min(rs), max(rs), min(cs), max(cs)
            H, W = r1-r0+1, maxc-minc+1
            aspect = abs(H-W)
            rel = [(p[0]-r0, p[1]-minc) for p in comp]
            info.append((aspect, minc, r0, H, W, rel))
        info.sort(key=lambda x:(x[0], x[2]))
        infos.append((color, info))
    infos.sort(key=lambda x: min(i[2] for i in x[1]))
    out = [[0]*w for _ in range(h)]
    for idx,(color,info) in enumerate(infos):
        _,_,_, Hs, Ws, rel_s = info[0]
        _,_,_, Hb, Wb, rel_b = info[1]
        b_sq = h - (Hs + Hb + 1)
        b_bar = h - Hb
        if idx==0:
            off_sq = 0
            off_bar = 0
        else:
            off_sq = w - Ws
            off_bar = w - Wb
        for dr,dc in rel_s:
            out[b_sq+dr][off_sq+dc] = color
        for dr,dc in rel_b:
            out[b_bar+dr][off_bar+dc] = color
    return out