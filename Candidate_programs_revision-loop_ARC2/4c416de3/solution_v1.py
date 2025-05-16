def solve(grid):
    H, W = len(grid), len(grid[0])
    from collections import Counter, deque
    cnt = Counter()
    for r in grid:
        cnt.update(r)
    bg = max(cnt, key=lambda k: cnt[k])
    zero = 0
    vis = [[False]*W for _ in range(H)]
    zones = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != bg and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j] = True
                cells = []
                while q:
                    r,c = q.popleft()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<H and 0<=nc<W and not vis[nr][nc] and grid[nr][nc]!=bg:
                            vis[nr][nc] = True
                            q.append((nr,nc))
                mr0 = min(r for r,c in cells)
                mr1 = max(r for r,c in cells)
                mc0 = min(c for r,c in cells)
                mc1 = max(c for r,c in cells)
                # expand box by 1 if possible to include zeros border
                r0 = max(0, mr0-1)
                c0 = max(0, mc0-1)
                r1 = min(H-1, mr1+1)
                c1 = min(W-1, mc1+1)
                h = r1-r0+1
                w = c1-c0+1
                # extract mask of colored (non-bg, non-zero) cells
                mask = [[1 if grid[r0+i][c0+j]!=bg and grid[r0+i][c0+j]!=zero else 0 for j in range(w)] for i in range(h)]
                # primary color = non-zero non-bg cell nearest center
                cr = (r0+r1)/2
                cc = (c0+c1)/2
                best = None; bd = None
                for r,c in cells:
                    v = grid[r][c]
                    if v!=zero and v!=bg:
                        d = (r-cr)**2 + (c-cc)**2
                        if bd is None or d<bd:
                            bd = d; best = v
                zones.append({'r0':r0,'c0':c0,'h':h,'w':w,'mask':mask,'color':best})
    zones.sort(key=lambda z:(z['r0'],z['c0']))
    def rotate_cw(m):
        h = len(m); w = len(m[0])
        return [[m[h-1-i][j] for i in range(h)] for j in range(w)]
    out = [row[:] for row in grid]
    N = len(zones)
    for i in range(N):
        prev = zones[i]
        nxt = zones[(i+1)%N]
        M = prev['mask']
        R = rotate_cw(M)
        if len(R)==nxt['h'] and len(R[0])==nxt['w']:
            for i0 in range(nxt['h']):
                for j0 in range(nxt['w']):
                    if R[i0][j0] and out[nxt['r0']+i0][nxt['c0']+j0]==bg:
                        out[nxt['r0']+i0][nxt['c0']+j0] = nxt['color']
    return out