def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                pts.setdefault(v, []).append((r, c))
    colors = list(pts.keys())
    mid = W / 2
    cent = {v: sum(c for r,c in pts[v]) / len(pts[v]) for v in colors}
    if cent[colors[0]] < mid <= cent[colors[1]]:
        left_color, right_color = colors[0], colors[1]
    elif cent[colors[1]] < mid <= cent[colors[0]]:
        left_color, right_color = colors[1], colors[0]
    else:
        if len(pts[colors[0]]) <= len(pts[colors[1]]):
            left_color, right_color = colors[0], colors[1]
        else:
            left_color, right_color = colors[1], colors[0]
    comps = {}
    for v in (left_color, right_color):
        seen = set()
        comp = []
        for p in pts[v]:
            if p in seen: continue
            stack = [p]
            seen.add(p)
            cur = []
            while stack:
                x,y = stack.pop()
                cur.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0<=nx<H and 0<=ny<W and (nx,ny) not in seen and grid[nx][ny]==v:
                        seen.add((nx,ny))
                        stack.append((nx,ny))
            comp.append(cur)
        a0, a1 = len(comp[0]), len(comp[1])
        if a0 <= a1:
            small, large = comp[0], comp[1]
        else:
            small, large = comp[1], comp[0]
        def stats(cells):
            rs = [r for r,c in cells]
            cs = [c for r,c in cells]
            return min(rs), max(rs), min(cs), max(cs), max(rs)-min(rs)+1, max(cs)-min(cs)+1
        mn0, mx0, mc0, MWC0, h0, w0 = stats(small)
        mn1, mx1, mc1, MWC1, h1, w1 = stats(large)
        comps[v] = (small, large, (mn0, mx0, mc0, w0, h0), (mn1, mx1, mc1, w1, h1))
    left_w = 0
    for side in comps[left_color][2:], comps[left_color][3:]:
        _,_,_,w,h = side
        left_w = max(left_w, w)
    out = [[0]*W for _ in range(H)]
    for v, side in ((left_color, 'L'), (right_color, 'R')):
        small, large, s0, s1 = comps[v]
        mn0, mx0, mc0, w0, h0 = s0
        mn1, mx1, mc1, w1, h1 = s1
        if side == 'L':
            sy0 = H//2 - mn0
            sx0 = 0 - mc0
            sy1 = H-1 - mx1
            sx1 = 0 - mc1
        else:
            base = left_w + 1
            sx1 = base - mc1
            sx0 = base + (w1 - w0) - mc0
            sy1 = H-1 - mx1
            sy0 = H//2 - mn0
        for r,c in small:
            out[r+sy0][c+sx0] = v
        for r,c in large:
            out[r+sy1][c+sx1] = v
    return out