def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    shapes = []
    for i in range(h-3):
        for j in range(w-3):
            c = grid[i][j]
            if c == 0: continue
            ok = True
            for dj in range(4):
                if grid[i][j+dj] != c or grid[i+3][j+dj] != c:
                    ok = False; break
            if not ok: continue
            for di in range(4):
                if grid[i+di][j] != c or grid[i+di][j+3] != c:
                    ok = False; break
            if not ok: continue
            if grid[i+1][j+1] or grid[i+1][j+2] or grid[i+2][j+1] or grid[i+2][j+2]:
                continue
            block = [row[j:j+4] for row in grid[i:i+4]]
            shapes.append((i, j, block))
    if not shapes:
        return []
    band_h = h // 3 if h >= 3 else h
    counts = [0, 0, 0]
    byband = {0: [], 1: [], 2: []}
    for i, j, blk in shapes:
        b = i // band_h if band_h else 0
        if b >= 3: b = 2
        counts[b] += 1
        byband[b].append((i, j, blk))
    m = max(counts)
    sel_bands = [b for b in range(3) if counts[b] == m]
    if len(sel_bands) == 1:
        chosen = byband[sel_bands[0]]
    elif len(sel_bands) == 2:
        chosen = byband[sel_bands[0]] + byband[sel_bands[1]]
    else:
        chosen = shapes
    # decide orientation
    chosen.sort(key=lambda x: x[1])
    horiz = True
    if len(sel_bands) == 2:
        horiz = False
    else:
        # check overlap in x
        ends = []
        for _, j, _ in chosen:
            if ends and j < ends[-1]:
                horiz = False
                break
            ends.append(j+4)
    if horiz:
        out = []
        for di in range(4):
            row = []
            for _, _, blk in chosen:
                row += blk[di]
            out.append(row)
    else:
        out = []
        for _, _, blk in chosen:
            out += blk
    return out