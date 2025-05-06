def solve(grid):
    H = len(grid)
    W = len(grid[0])
    counts = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                counts[v] = counts.get(v, 0) + 1
    stripe = max(counts, key=counts.get)
    stripe_rows = [r for r in range(H) if sum(1 for c in range(W) if grid[r][c] == stripe) > W//2]
    stripe_cols = [c for c in range(W) if sum(1 for r in range(H) if grid[r][c] == stripe) > H//2]
    stripe_rows.sort()
    stripe_cols.sort()
    rr = []
    prev = 0
    for r in stripe_rows:
        if r > prev:
            rr.append(list(range(prev, r)))
        prev = r + 1
    if prev < H:
        rr.append(list(range(prev, H)))
    cc = []
    prev = 0
    for c in stripe_cols:
        if c > prev:
            cc.append(list(range(prev, c)))
        prev = c + 1
    if prev < W:
        cc.append(list(range(prev, W)))
    row2br = [-1]*H
    for i,rs in enumerate(rr):
        for r in rs:
            row2br[r] = i
    col2bc = [-1]*W
    for j,cs in enumerate(cc):
        for c in cs:
            col2bc[c] = j
    pcols = set()
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v and v != stripe:
                pcols.add(v)
    for p in pcols:
        blocks = set()
        for r in range(H):
            for c in range(W):
                if grid[r][c] == p:
                    br = row2br[r]; bc = col2bc[c]
                    if br >= 0 and bc >= 0:
                        blocks.add((br, bc))
        if not blocks:
            continue
        minbr = min(b for b,_ in blocks)
        minbc = min(bc for _,bc in blocks)
        maxbr = minbr + 1
        maxbc = minbc + 1
        h = len(rr[minbr]); w = len(cc[minbc])
        P = [[1 if grid[r][c] == p else 0 for c in cc[minbc]] for r in rr[minbr]]
        for br in (minbr, maxbr):
            for bc in (minbc, maxbc):
                if (br, bc) not in blocks:
                    vflip = br > minbr
                    hflip = bc > minbc
                    for pr in range(h):
                        for pc in range(w):
                            if P[pr][pc]:
                                dr = h-1-pr if vflip else pr
                                dc = w-1-pc if hflip else pc
                                r0 = rr[br][dr]; c0 = cc[bc][dc]
                                grid[r0][c0] = p
    return grid