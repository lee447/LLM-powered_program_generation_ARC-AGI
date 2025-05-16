import collections

def solve(grid):
    H, W = len(grid), len(grid[0])
    bg = grid[0][0]
    red = 2
    dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
    visitedR = [[False]*W for _ in range(H)]
    red_comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == red and not visitedR[i][j]:
                comp = []
                dq = collections.deque([(i,j)])
                visitedR[i][j] = True
                while dq:
                    x,y = dq.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs4:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not visitedR[nx][ny] and grid[nx][ny]==red:
                            visitedR[nx][ny] = True
                            dq.append((nx,ny))
                red_comps.append(comp)
    def bfs4(sr,sc):
        val = grid[sr][sc]
        dq = collections.deque([(sr,sc)])
        seen = {(sr,sc)}
        while dq:
            x,y = dq.popleft()
            for dx,dy in dirs4:
                nx,ny = x+dx, y+dy
                if 0<=nx<H and 0<=ny<W and (nx,ny) not in seen and grid[nx][ny]==val:
                    seen.add((nx,ny))
                    dq.append((nx,ny))
        return seen
    out = [row[:] for row in grid]
    for comp in red_comps:
        if len(comp)==1:
            r0,c0 = comp[0]
            visitedS = [[False]*W for _ in range(H)]
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    if dr==0 and dc==0: continue
                    r1,c1 = r0+dr, c0+dc
                    if 0<=r1<H and 0<=c1<W and grid[r1][c1] not in (bg, red) and not visitedS[r1][c1]:
                        shape = bfs4(r1,c1)
                        for x,y in shape:
                            visitedS[x][y] = True
                        for x,y in shape:
                            rx, ry = 2*r0-x, 2*c0-y
                            if 0<=rx<H and 0<=ry<W and out[rx][ry]==bg:
                                out[rx][ry] = grid[x][y]
        else:
            rows = {r for r,c in comp}
            cols = {c for r,c in comp}
            if len(rows)==1:
                r0 = next(iter(rows))
                visitedS = [[False]*W for _ in range(H)]
                for side in (-1,1):
                    r1 = r0+side
                    if not (0<=r1<H): continue
                    for c in cols:
                        if grid[r1][c] not in (bg, red) and not visitedS[r1][c]:
                            shape = bfs4(r1,c)
                            for x,y in shape:
                                visitedS[x][y] = True
                            for x,y in shape:
                                rx, ry = 2*r0-x, y
                                if 0<=rx<H and 0<=ry<W and out[rx][ry]==bg:
                                    out[rx][ry] = grid[x][y]
            else:
                c0 = next(iter(cols))
                visitedS = [[False]*W for _ in range(H)]
                for side in (-1,1):
                    c1 = c0+side
                    if not (0<=c1<W): continue
                    for r in rows:
                        if grid[r][c1] not in (bg, red) and not visitedS[r][c1]:
                            shape = bfs4(r,c1)
                            for x,y in shape:
                                visitedS[x][y] = True
                            for x,y in shape:
                                rx, ry = x, 2*c0-y
                                if 0<=rx<H and 0<=ry<W and out[rx][ry]==bg:
                                    out[rx][ry] = grid[x][y]
    return out