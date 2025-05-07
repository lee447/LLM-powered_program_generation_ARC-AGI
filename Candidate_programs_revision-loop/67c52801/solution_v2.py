def solve(grid):
    m = len(grid)
    n = len(grid[0])
    last = grid[m-1]
    freq = {}
    for c in last:
        freq[c] = freq.get(c,0)+1
    bc = max(freq, key=lambda x: freq[x])
    supports = [j for j in range(n) if grid[m-2][j]==bc]
    supports.sort()
    windows = []
    for i in range(len(supports)-1):
        a, b = supports[i], supports[i+1]
        if b - a > 1:
            windows.append((a+1, b-1))
    shapes = {}
    for i in range(m):
        for j in range(n):
            c = grid[i][j]
            if c!=0 and c!=bc:
                if c not in shapes:
                    shapes[c] = [i,i,j,j]
                else:
                    shapes[c][0] = min(shapes[c][0],i)
                    shapes[c][1] = max(shapes[c][1],i)
                    shapes[c][2] = min(shapes[c][2],j)
                    shapes[c][3] = max(shapes[c][3],j)
    shape_list = []
    for c,(i1,i2,j1,j2) in shapes.items():
        h = i2-i1+1
        w = j2-j1+1
        shape_list.append([c,h,w])
    out = [[0]*n for _ in range(m)]
    for j in range(n):
        out[m-1][j] = bc
    for j in supports:
        out[m-2][j] = bc
    used = set()
    for g_start,g_end in windows:
        gw = g_end - g_start + 1
        for s in shape_list:
            c,h,w = s
            if c in used: continue
            if w==gw:
                hh,ww = h,w
            elif h==gw:
                hh,ww = w,h
            else:
                continue
            top = m-1-hh
            for di in range(hh):
                for dj in range(ww):
                    out[top+di][g_start+dj] = c
            used.add(c)
            break
    return out