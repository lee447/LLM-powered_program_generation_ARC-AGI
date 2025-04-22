def solve(grid):
    H, W = len(grid), len(grid[0])
    from collections import defaultdict, deque
    cells_by_color = defaultdict(set)
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0:
                cells_by_color[v].add((r, c))
    clusters_by_color = {}
    for color, cells in cells_by_color.items():
        remaining = set(cells)
        comps = []
        while remaining:
            sr, sc = remaining.pop()
            q = deque([(sr, sc)])
            comp = {(sr, sc)}
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r+dr, c+dc
                    if (nr, nc) in remaining:
                        remaining.remove((nr, nc))
                        comp.add((nr, nc))
                        q.append((nr, nc))
            comps.append(list(comp))
        clusters_by_color[color] = comps
    info = []
    for color, comps in clusters_by_color.items():
        cl = []
        for comp in comps:
            rs = [r for r,c in comp]
            cs = [c for r,c in comp]
            minr, maxr = min(rs), max(rs)
            minc, maxc = min(cs), max(cs)
            cl.append((minr, minc, maxr, maxc, comp))
        cl.sort(key=lambda x:(x[0], x[1]))
        minr1, minc1, maxr1, maxc1, comp1 = cl[0]
        minr2, minc2, maxr2, maxc2, comp2 = cl[1]
        h1, w1 = maxr1-minr1+1, maxc1-minc1+1
        h2, w2 = maxr2-minr2+1, maxc2-minc2+1
        info.append((color, (minr1,minc1,h1,w1,comp1), (minr2,minc2,h2,w2,comp2)))
    # decide left color by global mincol
    mins = [(min(c for r,c in cells_by_color[color]), color) for color,_,_ in info]
    left_color = min(mins)[1]
    out = [[0]*W for _ in range(H)]
    for color, cl1, cl2 in info:
        is_left = (color == left_color)
        minr1, minc1, h1, w1, comp1 = cl1
        minr2, minc2, h2, w2, comp2 = cl2
        top1 = H - (h1 + 1 + h2)
        top2 = top1 + h1 + 1
        for r, c in comp1:
            nr = top1 + (r - minr1)
            nc = (c - minc1) if is_left else (W - w1 + (c - minc1))
            out[nr][nc] = color
        for r, c in comp2:
            nr = top2 + (r - minr2)
            nc = (c - minc2) if is_left else (W - w2 + (c - minc2))
            out[nr][nc] = color
    return out