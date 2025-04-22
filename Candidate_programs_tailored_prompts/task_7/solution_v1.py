def solve(grid):
    H, W = len(grid), len(grid[0])
    from collections import deque
    colors = set()
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0:
                colors.add(grid[r][c])
    colors = list(colors)
    cells = {col: set() for col in colors}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                cells[v].add((r, c))
    clusters = {}
    for col in colors:
        rem = set(cells[col])
        cls = []
        while rem:
            start = rem.pop()
            q = deque([start])
            comp = {start}
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r+dr, c+dc
                    if (nr, nc) in rem:
                        rem.remove((nr, nc))
                        comp.add((nr, nc))
                        q.append((nr, nc))
            cls.append(list(comp))
        clusters[col] = cls
    info = {}
    for col in colors:
        a, b = clusters[col]
        def prop(cl):
            rs = [r for r,c in cl]; cs = [c for r,c in cl]
            return min(rs), max(rs), min(cs), max(cs), len(cl)
        r0a,r1a,c0a,c1a,la = prop(a)
        r0b,r1b,c0b,c1b,lb = prop(b)
        ha, wa = r1a-r0a+1, c1a-c0a+1
        hb, wb = r1b-r0b+1, c1b-c0b+1
        # classify small/big
        if ha < hb or (ha==hb and wa < wb) or (ha==hb and wa==wb and la < lb):
            small, big = (a, r0a,c0a,ha,wa), (b, r0b,c0b,hb,wb)
        else:
            small, big = (b, r0b,c0b,hb,wb), (a, r0a,c0a,ha,wa)
        info[col] = {'small': small, 'big': big}
    # order colors by overall mincol
    order = sorted(colors, key=lambda col: min(info[col]['small'][2], info[col]['big'][2]))
    offs = {}
    # horizontal offsets
    c0, c1 = order[0], order[1]
    ws0 = info[c0]['small'][4]; wb0 = info[c0]['big'][4]
    offs[c0] = 0
    offs[c1] = max(ws0, wb0) + 1
    # vertical offsets & fill
    out = [[0]*W for _ in range(H)]
    for col in order:
        small, r0s, c0s, hs, ws = info[col]['small']
        big, r0b, c0b, hb, wb = info[col]['big']
        big_start = H - hb
        small_start = big_start - 1 - hs
        # small
        for r,c in small:
            nr = small_start + (r - r0s)
            nc = offs[col] + (c - c0s)
            out[nr][nc] = col
        # big
        for r,c in big:
            nr = big_start + (r - r0b)
            nc = offs[col] + (c - c0b)
            out[nr][nc] = col
    return out