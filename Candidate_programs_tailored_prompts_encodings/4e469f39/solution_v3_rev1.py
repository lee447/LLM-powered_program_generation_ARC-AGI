import collections
def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not visited[i][j]:
                q = collections.deque([(i,j)])
                visited[i][j] = True
                pts = []
                while q:
                    r,c = q.popleft()
                    pts.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0<=rr<h and 0<=cc<w and not visited[rr][cc] and grid[rr][cc]==5:
                            visited[rr][cc] = True
                            q.append((rr,cc))
                rs = [r for r,c in pts]; cs = [c for r,c in pts]
                comps.append({'r1':min(rs),'r2':max(rs),'c1':min(cs),'c2':max(cs)})
    comps.sort(key=lambda x: x['c1'])
    for comp in comps:
        r1,r2,c1,c2 = comp['r1'],comp['r2'],comp['c1'],comp['c2']
        for r in range(r1+1, r2):
            for c in range(c1+1, c2):
                if res[r][c] != 5:
                    res[r][c] = 2
    holes = []
    for comp in comps:
        r1,c1,c2 = comp['r1'], comp['c1'], comp['c2']
        hc = [c for c in range(c1, c2+1) if grid[r1][c]==0]
        holes.append({'r':r1, 'cols':hc})
        for c in hc:
            res[r1][c] = 2
    if len(comps)==1:
        comp = comps[0]; r1 = comp['r1']
        hc = holes[0]['cols']
        width = comp['c2']-comp['c1']+1
        if hc:
            if len(hc)==1:
                start = 0; length = width+1
            else:
                start = min(hc); length = w-start
            row = r1-1
            if 0<=row<h:
                for c in range(start, start+length):
                    res[row][c] = 2
    else:
        for i, comp in enumerate(comps):
            r1 = comp['r1']
            hc = holes[i]['cols']
            if not hc: continue
            if i==0:
                start = min(hc); length = w-start
            elif i==len(comps)-1:
                start = 0; length = max(hc)+1
            else:
                continue
            row = r1-1
            if 0<=row<h:
                for c in range(start, start+length):
                    res[row][c] = 2
    return res