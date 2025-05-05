def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                c = grid[i][j]
                stack = [(i,j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                comps.append((c,comp))
    frames = []
    for c,pts in comps:
        rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
        r0,r1 = min(rs), max(rs)
        c0,c1 = min(cs), max(cs)
        # build hollow border of 4x4
        border = []
        for rr in range(r0, r1+1):
            for cc in range(c0, c1+1):
                if rr in (r0,r1) or cc in (c0,c1):
                    border.append((rr,cc))
        frames.append({
            'color': c,
            'r0': r0, 'r1': r1,
            'c0': c0, 'c1': c1,
            'border': border
        })
    m = len(frames)
    k = m//2
    def intersect_range(a0,a1,b0,b1):
        return not (a1 < b0 or b1 < a0)
    # try row cluster
    from itertools import combinations
    sel = None
    dim = None
    for comb in combinations(range(m), k):
        rr0 = max(frames[i]['r0'] for i in comb)
        rr1 = min(frames[i]['r1'] for i in comb)
        if rr0 <= rr1:
            sel = comb; dim = 'row'; break
    if sel is None:
        for comb in combinations(range(m), k):
            cc0 = max(frames[i]['c0'] for i in comb)
            cc1 = min(frames[i]['c1'] for i in comb)
            if cc0 <= cc1:
                sel = comb; dim = 'col'; break
    chosen = [frames[i] for i in sel]
    if dim == 'row':
        chosen.sort(key=lambda f: f['c0'])
        H = 4; W = 4*k
        out = [[0]*W for _ in range(H)]
        for idx,f in enumerate(chosen):
            dr = f['r0']
            dc = idx*4 - f['c0']
            for x,y in f['border']:
                out[x-dr][y+dc] = f['color']
    else:
        chosen.sort(key=lambda f: f['r0'])
        H = 4*k; W = 4
        out = [[0]*W for _ in range(H)]
        for idx,f in enumerate(chosen):
            dr = idx*4 - f['r0']
            dc = f['c0']
            for x,y in f['border']:
                out[x+dr][y-dc] = f['color']
    return out