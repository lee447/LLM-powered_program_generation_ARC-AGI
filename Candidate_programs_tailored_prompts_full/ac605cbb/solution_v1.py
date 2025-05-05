def solve(grid):
    H, W = len(grid), len(grid[0])
    anchors = [(r, c, grid[r][c]) for r in range(H) for c in range(W) if grid[r][c] != 0]
    out = [[0]*W for _ in range(H)]
    occupied = [[False]*W for _ in range(H)]
    for r, c, v in anchors:
        out[r][c] = v
        occupied[r][c] = True
    for r, c, v in anchors:
        placed = False
        for order in [(0,1),(1,0)]:
            if placed: break
            for hd in (-1,1):
                if placed: break
                for vd in (-1,1):
                    if placed: break
                    maxh = (W-1-c) if hd>0 else c
                    maxv = (H-1-r) if vd>0 else r
                    if maxh<0 or maxv<0: continue
                    for hlen in range(1, maxh+1):
                        for vlen in range(1, maxv+1):
                            if order[0]==0:
                                hr, hc = r, c+hd*hlen
                                vr, vc = hr+vd*vlen, hc
                                path1 = [(r, c+hd*i) for i in range(1, hlen+1)]
                                corner = (hr, hc)
                                path2 = [(hr+vd*i, hc) for i in range(1, vlen+1)]
                            else:
                                vr, vc = r+vd*vlen, c
                                hr, hc = vr, c+hd*hlen
                                path1 = [(r+vd*i, c) for i in range(1, vlen+1)]
                                corner = (vr, vc)
                                path2 = [(vr, c+hd*i) for i in range(1, hlen+1)]
                            if not (0<=vr<H and 0<=vc<W): continue
                            ok = True
                            for x,y in path1+path2:
                                if occupied[x][y]: ok=False; break
                            if occupied[vr][vc]: ok=False
                            if not ok: continue
                            for x,y in path1: out[x][y]=5; occupied[x][y]=True
                            if hlen>0 and vlen>0:
                                x,y = corner
                                out[x][y]=4; occupied[x][y]=True
                            for x,y in path2: out[x][y]=5; occupied[x][y]=True
                            out[vr][vc]=v; occupied[vr][vc]=True
                            placed = True
                            break
        if not placed:
            # straight vertical
            for vd in (-1,1):
                maxv = (H-1-r) if vd>0 else r
                for vlen in range(1, maxv+1):
                    cells = [(r+vd*i,c) for i in range(1,vlen+1)]
                    if any(occupied[x][y] for x,y in cells): break
                    out[r+vd*vlen][c]=v
                    for x,y in cells:
                        out[x][y]=5; occupied[x][y]=True
                    occupied[r+vd*vlen][c]=True
                    placed=True
                    break
            if placed: continue
            # straight horizontal
            for hd in (-1,1):
                maxh = (W-1-c) if hd>0 else c
                for hlen in range(1, maxh+1):
                    cells = [(r,c+hd*i) for i in range(1,hlen+1)]
                    if any(occupied[x][y] for x,y in cells): break
                    out[r][c+hd*hlen]=v
                    for x,y in cells:
                        out[x][y]=5; occupied[x][y]=True
                    occupied[r][c+hd*hlen]=True
                    placed=True
                    break
    return out