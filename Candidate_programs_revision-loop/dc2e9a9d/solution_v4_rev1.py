from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not vis[i][j]:
                q = deque([(i,j)]); vis[i][j]=True
                cells = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==3:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                            cells.append((nx,ny))
                rs = [x for x,y in cells]; cs = [y for x,y in cells]
                r0,r1,c0,c1 = min(rs),max(rs),min(cs),max(cs)
                hh,ww = r1-r0+1, c1-c0+1
                if hh%2==1 and ww%2==1:
                    mask = [[grid[r0+ii][c0+jj]==3 for jj in range(ww)] for ii in range(hh)]
                    comps.append((hh*ww, r0, c0, hh, ww, mask))
    comps.sort(reverse=True)
    if len(comps)<2:
        return grid
    _, br0, bc0, bh, bw, bmask = comps[0]
    _, sr0, sc0, sh, sw, smask = comps[1]
    out = [row[:] for row in grid]
    tr0_b, tc0_b = br0, bc0 + bw + 1
    for ii in range(bh):
        for jj in range(bw):
            if bmask[ii][jj]:
                x,y = tr0_b+ii, tc0_b+jj
                if 0<=x<h and 0<=y<w:
                    out[x][y] = 1
    tr0_s, tc0_s = br0 + bh + 1, bc0 + bw - 1
    for ii in range(sh):
        for jj in range(sw):
            if smask[ii][jj]:
                x,y = tr0_s+ii, tc0_s+jj
                if 0<=x<h and 0<=y<w:
                    out[x][y] = 8
    return out