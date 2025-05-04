def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def inb(y,x): return 0<=y<h and 0<=x<w
    vis = [[False]*w for _ in range(h)]
    bars = []
    for y in range(h):
        for x in range(w):
            if grid[y][x]==5 and not vis[y][x]:
                comp = [(y,x)]
                vis[y][x]=True
                qi=0
                while qi<len(comp):
                    cy,cx = comp[qi]; qi+=1
                    for dy,dx in dirs:
                        ny,nx = cy+dy,cx+dx
                        if inb(ny,nx) and not vis[ny][nx] and grid[ny][nx]==5:
                            vis[ny][nx]=True
                            comp.append((ny,nx))
                ys = [p[0] for p in comp]; xs = [p[1] for p in comp]
                if len(set(xs))==1: orient='vert'
                else: orient='horiz'
                bars.append((orient,comp))
    out = [row[:] for row in grid]
    for orient,comp in bars:
        if orient=='vert':
            bar_cells = sorted(comp, key=lambda p:p[0])
            checks = [(0,1),(0,-1)]
        else:
            bar_cells = sorted(comp, key=lambda p:p[1])
            checks = [(1,0),(-1,0)]
        strip_dir = None
        for d in checks:
            if any(inb(y+d[0],x+d[1]) and grid[y+d[0]][x+d[1]] not in (0,5) for y,x in bar_cells):
                strip_dir = d
                break
        sb_vis = [[False]*w for _ in range(h)]
        strips = []
        for y,x in bar_cells:
            ny, nx = y+strip_dir[0], x+strip_dir[1]
            if inb(ny,nx) and grid[ny][nx] not in (0,5) and not sb_vis[ny][nx]:
                comp2 = [(ny,nx)]
                sb_vis[ny][nx]=True
                qi=0
                while qi<len(comp2):
                    cy,cx = comp2[qi]; qi+=1
                    for dy,dx in dirs:
                        ay,ax = cy+dy,cx+dx
                        if inb(ay,ax) and not sb_vis[ay][ax] and grid[ay][ax] not in (0,5):
                            # ensure stays in strip direction zone
                            if (strip_dir[0]==0 and ay==ny) or (strip_dir[1]==0 and ax==nx):
                                sb_vis[ay][ax]=True
                                comp2.append((ay,ax))
                strips.append(comp2)
        if not strips: continue
        # sort strips along bar axis
        if orient=='vert':
            strips.sort(key=lambda comp2: comp2[0][0])
        else:
            strips.sort(key=lambda comp2: comp2[0][1])
        pattern_blocks = []
        for comp2 in strips:
            ys = [p[0] for p in comp2]; xs = [p[1] for p in comp2]
            if len(set(ys))==1:
                ry = ys[0]
                row = sorted(xs)
                pattern = [grid[ry][cx] for cx in row]
                start = row[0]
            else:
                cx = xs[0]
                col = sorted(ys)
                pattern = [grid[ry][cx] for ry in col]
                start = col[0]
            pattern_blocks.append((pattern,start))
        M = len(pattern_blocks)
        # all blocks same length?
        L = len(pattern_blocks[0][0])
        if orient=='vert':
            for i,(y,x) in enumerate(bar_cells):
                pat, sx = pattern_blocks[i%M]
                for j in range(L):
                    out[y][sx+j] = pat[j]
        else:
            for i,(y,x) in enumerate(bar_cells):
                pat, sy = pattern_blocks[i%M]
                for j in range(L):
                    out[sy+j][x] = pat[j]
    return out