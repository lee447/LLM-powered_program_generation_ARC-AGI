from collections import deque, defaultdict

def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                cells = []
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]!=0:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                rs = [r for r,c in cells]
                cs = [c for r,c in cells]
                r0,r1,c0,c1 = min(rs),max(rs),min(cs),max(cs)
                h,w = r1-r0+1, c1-c0+1
                if w>1 and len(cells)==h*w:
                    comps.append((r0,c0,h,w,cells))
    by_size = defaultdict(list)
    y_off = defaultdict(set)
    for r0,c0,h,w,cells in comps:
        by_size[(h,w)].append(cells)
        y_off[(h,w)].add(r0)
    sizes = [sz for sz in by_size if len(y_off[sz])>1]
    out = [[0]*W for _ in range(H)]
    for sz in sizes:
        for cells in by_size[sz]:
            for r,c in cells:
                out[r][c] = grid[r][c]
    return out