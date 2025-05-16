def solve(grid):
    h, w = len(grid), len(grid[0])
    border = []
    for i in range(w):
        border.append(grid[0][i])
        border.append(grid[h-1][i])
    for i in range(h):
        border.append(grid[i][0])
        border.append(grid[i][w-1])
    from collections import Counter, deque
    bg = Counter(border).most_common(1)[0][0]
    seen = [[False]*w for _ in range(h)]
    frames = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]==0 and not seen[r][c]:
                q = deque([(r,c)])
                cc = []
                seen[r][c]=True
                while q:
                    x,y = q.popleft()
                    cc.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==0:
                            seen[nx][ny]=True
                            q.append((nx,ny))
                rs = [x for x,_ in cc]; cs = [y for _,y in cc]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                per = (r1-r0+1)*2 + (c1-c0+1)*2 - 4
                if len(cc)==per and r1-r0>=2 and c1-c0>=2:
                    frames.append((r0,r1,c0,c1))
    cx, cy = (w-1)/2, (h-1)/2
    def center(f):
        r0,r1,c0,c1 = f
        return ((r0+r1)/2, (c0+c1)/2)
    def angle(f):
        ry, rx = center(f)
        return -(__import__('math').atan2(ry-cy, rx-cx))
    frames.sort(key=angle)
    pats = []
    for r0,r1,c0,c1 in frames:
        H, W = r1-r0-1, c1-c0-1
        P = [grid[r0+1+i][c0+1:c1] for i in range(H)]
        pats.append(P)
    newp = pats[-1:]+pats[:-1]
    def rot90(P):
        return [ [P[len(P)-1-i][j] for i in range(len(P))] for j in range(len(P[0])) ]
    for (r0,r1,c0,c1), P in zip(frames, newp):
        H, W = r1-r0-1, c1-c0-1
        for _ in range(4):
            if len(P)==H and len(P[0])==W: break
            P = rot90(P)
        for i in range(len(P)):
            for j in range(len(P[0])):
                v = P[i][j]
                if v==5: v = 7
                elif v==7: v = 5
                grid[r0+1+i][c0+1+j] = v
    return grid