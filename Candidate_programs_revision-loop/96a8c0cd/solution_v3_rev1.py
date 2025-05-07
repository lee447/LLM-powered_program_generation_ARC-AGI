from collections import deque, defaultdict

def solve(grid):
    H, W = len(grid), len(grid[0])
    M = [[cell if cell != 2 else 0 for cell in row] for row in grid]
    visited = [[False]*W for _ in range(H)]
    shapes = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] not in (0,2) and not visited[i][j]:
                c = grid[i][j]
                q = deque([(i,j)])
                visited[i][j] = True
                cells = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == c:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                rs = [r for r,_ in cells]
                cs = [cc for _,cc in cells]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                cr = (r0 + r1)//2
                cc = (c0 + c1)//2
                shapes.append((c, cr, cc))
    by_color = defaultdict(list)
    for c,cr,cc in shapes:
        by_color[c].append((cr,cc))
    for centers in by_color.values():
        rows = defaultdict(list)
        cols = defaultdict(list)
        for r,c in centers:
            rows[r].append(c)
            cols[c].append(r)
        for r, clist in rows.items():
            if len(clist)>1:
                clist.sort()
                for a,b in zip(clist, clist[1:]):
                    for y in range(a+1, b):
                        if M[r][y]==0: M[r][y]=2
        for c, rlist in cols.items():
            if len(rlist)>1:
                rlist.sort()
                for a,b in zip(rlist, rlist[1:]):
                    for x in range(a+1, b):
                        if M[x][c]==0: M[x][c]=2
    return M