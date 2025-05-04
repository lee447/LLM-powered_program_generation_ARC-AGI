def solve(grid):
    h0, w0 = len(grid), len(grid[0])
    # find background color
    from collections import deque
    bg = None
    cnt = {}
    for i in range(h0):
        for j in (0, w0-1):
            v = grid[i][j]
            cnt[v] = cnt.get(v, 0) + 1
    for j in range(w0):
        for i in (0, h0-1):
            v = grid[i][j]
            cnt[v] = cnt.get(v, 0) + 1
    bg = max(cnt, key=cnt.get)
    # find components
    visited = [[False]*w0 for _ in range(h0)]
    comps = []
    for i in range(h0):
        for j in range(w0):
            if grid[i][j] != bg and not visited[i][j]:
                col = grid[i][j]
                q = deque([(i,j)])
                visited[i][j] = True
                cells = []
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h0 and 0<=ny<w0 and not visited[nx][ny] and grid[nx][ny]==col:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                comps.append((cells, col))
    comps.sort(key=lambda x: len(x[0]))
    small, med, large = comps[0], comps[1], comps[2]
    def extract(comp):
        cells, col = comp
        rs = [r for r,c in cells]; cs = [c for r,c in cells]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        H, W = r1-r0+1, c1-c0+1
        m = [[0]*W for _ in range(H)]
        for r,c in cells:
            m[r-r0][c-c0] = col
        return m
    m_s = extract(small)
    m_m = extract(med)
    m_L = extract(large)
    # rotate largest 180
    m_L = [row[::-1] for row in m_L[::-1]]
    H, W = len(m_L), len(m_L[0])
    res = [[bg]*W for _ in range(H)]
    for m in (m_m, m_s, m_L):
        hh, ww = len(m), len(m[0])
        for i in range(hh):
            for j in range(ww):
                if m[i][j] != 0:
                    res[i][j] = m[i][j]
    return res