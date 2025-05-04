def solve(grid):
    H = len(grid)
    W = len(grid[0])
    br = []
    for i in range(H):
        s = set(grid[i])
        if len(s) == 1 and next(iter(s)) != 0:
            br.append(i)
    br.sort()
    fc = grid[br[0]][0]
    stripe_w = 0
    for c in range(W):
        ok = True
        for r in br:
            if grid[r][c] != fc:
                ok = False; break
        if ok:
            stripe_w += 1
        else:
            break
    seen = [[False]*W for _ in range(H)]
    clusters = []
    for y in range(H):
        for x in range(stripe_w, W):
            v = grid[y][x]
            if v != 0 and v != fc and not seen[y][x]:
                col = v
                q = [(y,x)]
                seen[y][x] = True
                pts = []
                mi, ma = y, y
                mj, mb = x, x
                for yy,xx in q:
                    pts.append((yy,xx))
                    mi = min(mi, yy); ma = max(ma, yy)
                    mj = min(mj, xx); mb = max(mb, xx)
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < H and 0 <= nx < W and not seen[ny][nx]:
                            if grid[ny][nx] == col:
                                seen[ny][nx] = True
                                q.append((ny,nx))
                mask = [(yy-mi, xx-mj) for yy,xx in pts]
                clusters.append((mi, mj, ma, mb, col, mask))
    bands = len(br)-1
    old = [None]*bands
    for cl in clusters:
        mi, mj, ma, mb, col, mask = cl
        cy = (mi+ma)/2.0
        for k in range(bands):
            if br[k] < cy < br[k+1]:
                old[k] = cl
                break
    colors = [cl[4] for cl in old]
    med = sorted(colors)[1]
    if fc < med:
        mp = [1,2,0]
    else:
        mp = [2,1,0]
    out = [[fc]*stripe_w for _ in range(H)]
    for i in range(bands):
        mi, mj, ma, mb, col, mask = old[mp[i]]
        bh = br[i+1] - br[i] - 1
        ch = ma - mi + 1
        shift_y = br[i] + 1
        cw = mb - mj + 1
        shift_x = (stripe_w - cw)//2
        for dy,dx in mask:
            out[shift_y+dy][shift_x+dx] = col
    return out