from collections import Counter, deque
def solve(grid):
    R, C = len(grid), len(grid[0])
    cnt = Counter(grid[r][c] for r in range(R) for c in range(C))
    bg = cnt.most_common(1)[0][0]
    seen = [[False]*C for _ in range(R)]
    comps = []
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
                        if 0 <= nx < R and 0 <= ny < C and not seen[nx][ny] and grid[nx][ny] == col:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                h, w = r1-r0+1, c1-c0+1
                border_ok = all(grid[r][c] != bg for r in (r0, r1) for c in range(c0, c1+1)) and all(grid[r][c] != bg for r in range(r0, r1+1) for c in (c0, c1))
                if border_ok:
                    comps.append((h*w, r0, r1, c0, c1))
    if not comps:
        return grid
    _, r0, r1, c0, c1 = min(comps, key=lambda x: x[0])
    h, w = r1-r0+1, c1-c0+1
    T = [row[c0:c1+1] for row in grid[r0:r1+1]]
    top_drop = h if all(grid[0][j]==bg for j in range(C)) and all(grid[-1][j]==bg for j in range(C)) else 0
    left_drop = w if all(grid[i][0]==bg for i in range(R)) and all(grid[i][-1]==bg for i in range(R)) else 0
    outR = R - top_drop
    outC = C - left_drop
    out = [[bg]*outC for _ in range(outR)]
    for i in range(0, outR, h):
        for j in range(0, outC, w):
            for di in range(h):
                for dj in range(w):
                    if i+di < outR and j+dj < outC:
                        out[i+di][j+dj] = T[di][dj]
    return out