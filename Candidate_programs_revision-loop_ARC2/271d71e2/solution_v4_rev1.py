import math
from collections import Counter, deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    border = []
    for j in range(w):
        border.append(grid[0][j]); border.append(grid[h-1][j])
    for i in range(h):
        border.append(grid[i][0]); border.append(grid[i][w-1])
    bg = Counter(border).most_common(1)[0][0]
    S = {0,5,7}
    seen = [[False]*w for _ in range(h)]
    frames = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] in S and not seen[i][j]:
                dq = deque([(i,j)]); seen[i][j] = True
                cc = []
                while dq:
                    x,y = dq.popleft(); cc.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny] in S:
                            seen[nx][ny] = True
                            dq.append((nx,ny))
                rs = [x for x,_ in cc]; cs = [y for _,y in cc]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                H, W = r1-r0+1, c1-c0+1
                if H>=3 and W>=3 and len(cc)==H*W:
                    frames.append((r0,r1,c0,c1))
    if not frames:
        return grid
    cy, cx = (h-1)/2, (w-1)/2
    def ang(f):
        r0,r1,c0,c1 = f
        ry, rx = (r0+r1)/2, (c0+c1)/2
        return -math.atan2(ry-cy, rx-cx)
    frames.sort(key=ang)
    pats = []
    dims = []
    for r0,r1,c0,c1 in frames:
        P = [grid[r][c0+1:c1] for r in range(r0+1,r1)]
        pats.append(P)
        dims.append((r1-r0-1, c1-c0-1))
    n = len(frames)
    newp = pats[-1:]+pats[:-1]
    if n>1:
        k = n; step = 2*math.pi/k
    else:
        k = 4; step = math.pi/2
    new_frames = []
    for r0,r1,c0,c1 in frames:
        ry, rx = (r0+r1)/2, (c0+c1)/2
        dy, dx = ry-cy, rx-cx
        theta = math.atan2(dy,dx) + step
        d = math.hypot(dy,dx)
        nry = cy + math.sin(theta)*d
        nrx = cx + math.cos(theta)*d
        H, W = r1-r0, c1-c0
        nr0 = round(nry - H/2); nr1 = nr0 + H
        nc0 = round(nrx - W/2); nc1 = nc0 + W
        new_frames.append((nr0,nr1,nc0,nc1))
    for r0,r1,c0,c1 in frames:
        for i in range(r0,r1+1):
            for j in range(c0,c1+1):
                if i==r0 or i==r1 or j==c0 or j==c1:
                    grid[i][j] = bg
    def rot90(P):
        return [[P[len(P)-1-i][j] for i in range(len(P))] for j in range(len(P[0]))]
    for (r0,r1,c0,c1), P_old, P_new in zip(new_frames, pats, newp):
        H, W = r1-r0-1, c1-c0-1
        Q = P_new
        for _ in range(4):
            if len(Q)==H and len(Q[0])==W:
                break
            Q = rot90(Q)
        for i in range(H):
            for j in range(W):
                v = Q[i][j]
                if v==5: v = 7
                elif v==7: v = 5
                grid[r0+1+i][c0+1+j] = v
    return grid