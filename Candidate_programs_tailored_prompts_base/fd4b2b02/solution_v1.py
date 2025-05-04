def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    rs = [r for r,_ in pts]; cs = [c for _,c in pts]
    r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
    h, w = r1-r0+1, c1-c0+1
    M = [[1 if grid[r0+i][c0+j] != 0 else 0 for j in range(w)] for i in range(h)]
    c1col = grid[r0][c0]
    c2col = 9 - c1col
    # rotate M 90° CW => M2 of size w x h
    M2 = [[M[h-1-j][i] for j in range(h)] for i in range(w)]
    out = [[0]*W for _ in range(H)]
    # edge anchors for unrotated
    edges = []
    edges.append((0,       W//2 - w//2))
    edges.append((H - h,   W//2 - w//2))
    edges.append((H//2 - h//2, 0))
    edges.append((H//2 - h//2, W - w))
    for (rr, cc) in edges:
        for i in range(h):
            for j in range(w):
                if M[i][j]:
                    out[rr+i][cc+j] = c1col
    # quadrant centers for rotated
    Qs = []
    hh, ww = w, h
    midr, midc = H//2, W//2
    Qs.append(((0 + midr)//2 - hh//2, (0 + midc)//2 - ww//2))
    Qs.append(((0 + midr)//2 - hh//2, (midc + W)//2 - ww//2))
    Qs.append(((midr + H)//2 - hh//2, (0 + midc)//2 - ww//2))
    Qs.append(((midr + H)//2 - hh//2, (midc + W)//2 - ww//2))
    for (rr, cc) in Qs:
        for i in range(hh):
            for j in range(ww):
                if M2[i][j]:
                    out[rr+i][cc+j] = c2col
    return out