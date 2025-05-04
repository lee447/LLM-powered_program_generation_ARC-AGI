def solve(grid):
    H = len(grid)
    W = len(grid[0])
    header_row = None
    for r in range(H):
        vals = {grid[r][c] for c in range(W) if grid[r][c] not in (0,5)}
        if len(vals) >= 3 and any(v != 1 for v in vals):
            header_row = r
            break
    hdr = [(c, grid[header_row][c]) for c in range(W) if grid[header_row][c] not in (0,5)]
    hdr.sort()
    hdr_cols = [c for c,_ in hdr]
    hdr_cols_set = set(hdr_cols)
    hdr_colors = [col for _,col in hdr]
    pr = None
    for r in range(header_row+1, H):
        if any(grid[r][c] == 5 for c in range(W)):
            pr = r
            break
    pairs = []
    c = 0
    while c < W-1:
        if grid[pr][c] == 5 and grid[pr][c+1] == 5:
            pairs.append((c, c+1))
            c += 2
        else:
            c += 1
    pillars = []
    for pc in pairs:
        xs = []
        for r in range(header_row+1, H):
            for c in pc:
                v = grid[r][c]
                if v not in (0,5):
                    xs.append((r,c,v))
        if xs:
            pillars.append((pc, xs))
    # map header to pillar in left-to-right order
    pillars.sort(key=lambda x: x[0][0])
    n = min(len(hdr_colors), len(pillars))
    mapping = []
    for i in range(n):
        pc, pts = pillars[i]
        # pick two nearest pts
        pts = sorted(pts)
        if len(pts) >= 2:
            p1, p2 = pts[0], pts[1]
        else:
            p1 = pts[0]
            # find any neighbor
            found = None
            for dr,dc in ((0,1),(1,0),(-1,0),(0,-1)):
                rr,cc = p1[0]+dr, p1[1]+dc
                if 0 <= rr < H and 0 <= cc < W and grid[rr][cc]==p1[2]:
                    found = (rr,cc,p1[2])
                    break
            if found:
                p2 = found
            else:
                p2 = p1
        mapping.append((hdr_colors[i], pc, p1, p2))
    centers = []
    for _,pc,_,_ in mapping:
        centers.append((pc[0]+pc[1])/2)
    mn = min(centers)
    mx = max(centers) if len(centers)>1 else mn+1
    out_w = int(round(mx - mn)) + 2
    out = [[0]*out_w for _ in range(8)]
    for color, pc, p1, p2 in mapping:
        if p1[0] == p2[0]:
            ro = 0
        else:
            ro = 6
        cc = (p1[1]+p2[1])/2
        if cc < (pc[0]+pc[1])/2:
            co = 0
        else:
            co = out_w - 2
        for dr in (0,1):
            for dc in (0,1):
                out[ro+dr][co+dc] = color
    return out