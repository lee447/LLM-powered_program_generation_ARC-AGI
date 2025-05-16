from collections import Counter, deque

def solve(grid):
    R, C = len(grid), len(grid[0])
    bg = Counter(v for row in grid for v in row).most_common(1)[0][0]
    seen = [[False]*C for _ in range(R)]
    comps_all = []
    comps_good = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != bg and not seen[i][j]:
                col = grid[i][j]
                q = deque([(i,j)])
                seen[i][j] = True
                pts = []
                while q:
                    x,y = q.popleft()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<R and 0<=ny<C and not seen[nx][ny] and grid[nx][ny]==col:
                            seen[nx][ny]=True
                            q.append((nx,ny))
                rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                comps_all.append((r0,r1,c0,c1))
                h, w = r1-r0+1, c1-c0+1
                border = True
                for c in range(c0,c1+1):
                    if grid[r0][c]==bg or grid[r1][c]==bg:
                        border=False; break
                for r in range(r0,r1+1):
                    if grid[r][c0]==bg or grid[r][c1]==bg:
                        border=False; break
                if border:
                    comps_good.append((r0,r1,c0,c1))
    if not comps_good:
        return grid
    r0T,r1T,c0T,c1T = comps_good[0]
    hT, wT = r1T-r0T+1, c1T-c0T+1
    T = [row[c0T:c1T+1] for row in grid[r0T:r1T+1]]
    bad = [b for b in comps_all if b!=(r0T,r1T,c0T,c1T)]
    outR, outC = R, C
    if bad:
        r0b,r1b,c0b,c1b = bad[0]
        hb, wb = r1b-r0b+1, c1b-c0b+1
        if wb>hb:
            outR = R-hb
        elif hb>wb:
            outC = C-wb
    out = [[bg]*outC for _ in range(outR)]
    for i in range(0,outR,hT):
        for j in range(0,outC,wT):
            for di in range(hT):
                for dj in range(wT):
                    if i+di<outR and j+dj<outC:
                        out[i+di][j+dj] = T[di][dj]
    return out