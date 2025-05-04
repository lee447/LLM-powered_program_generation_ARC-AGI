def solve(grid):
    h = len(grid)
    w = len(grid[0])
    blocks = []
    for r in range(h-3):
        for c in range(w-3):
            v = grid[r][c]
            if v == 0: continue
            ok = True
            for i in range(4):
                for j in range(4):
                    val = grid[r+i][c+j]
                    if i in (0,3) or j in (0,3):
                        if val != v:
                            ok = False
                            break
                    else:
                        if val != 0:
                            ok = False
                            break
                if not ok: break
            if ok:
                blocks.append((r,c,v))
    bands = [[] for _ in range(3)]
    for b in blocks:
        r, c, v = b
        band = min((r * 3) // h, 2)
        bands[band].append(b)
    sizes = [len(bands[i]) for i in range(3)]
    m = max(sizes)
    sel = [i for i in range(3) if sizes[i] == m]
    def render(bs):
        if not bs:
            return []
        if len(bs) > 1 and all(bs[i][0] == bs[0][0] for i in range(len(bs))):
            bs_sorted = sorted(bs, key=lambda x: x[1])
            out = [[] for _ in range(4)]
            for _, c, v in bs_sorted:
                for i in range(4):
                    out[i].extend(grid[bs_sorted[0][0]+i][c:c+4])
            return out
        elif len(bs) > 1:
            bs_sorted = sorted(bs, key=lambda x: x[0])
            out = []
            for r, c, v in bs_sorted:
                for i in range(4):
                    out.append(grid[r+i][c:c+4])
            return out
        else:
            r, c, v = bs[0]
            return [row[c:c+4] for row in grid[r:r+4]]
    if len(sel) == 1:
        img = render(bands[sel[0]])
    else:
        img1 = render(bands[sel[0]])
        img2 = render(bands[sel[1]])
        img = img1 + img2
    return img