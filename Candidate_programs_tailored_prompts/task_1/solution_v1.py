def solve(grid):
    H = len(grid)
    W = len(grid[0])
    has6 = has1 = has8 = False
    for r in grid:
        for v in r:
            if v == 6: has6 = True
            if v == 1: has1 = True
            if v == 8: has8 = True
    if has6:
        # T1
        anchor = []
        for i in range(H):
            segs = []
            c = 0
            while c < W:
                if grid[i][c] == 6:
                    s = c
                    while c < W and grid[i][c] == 6:
                        c += 1
                    if c - s >= 6:
                        segs.append(s)
                else:
                    c += 1
            if len(segs) >= 2:
                anchor.append((i, segs))
        if not anchor:
            return [[0]*W for _ in range(H)]
        a0, cols = anchor[0]
        pat_h = 5
        pattern = [[0]*W for _ in range(pat_h)]
        for dr in range(pat_h):
            r = a0 + dr
            if r < 0 or r >= H: continue
            if dr == 0:
                for s in cols:
                    for dc in range(6):
                        c = s + dc
                        if 0 <= c < W:
                            pattern[dr][c] = 6
            else:
                for s in cols:
                    for dc in range(6):
                        c = s + dc
                        if 0 <= c < W:
                            v = grid[r][c]
                            if v == 8 or v == 3:
                                pattern[dr][c] = v
        out = [[0]*W for _ in range(H)]
        for a, _ in anchor:
            for dr in range(pat_h):
                r = a + dr
                if 0 <= r < H:
                    for c in range(W):
                        v = pattern[dr][c]
                        if v:
                            out[r][c] = v
        return out
    elif has8 and has1:
        # T2
        band = []
        for i in range(H):
            segs = []
            c = 0
            while c < W:
                if grid[i][c] == 8:
                    s = c
                    while c < W and grid[i][c] == 8:
                        c += 1
                    if c - s >= 5:
                        segs.append(s)
                else:
                    c += 1
            if len(segs) >= 2:
                band.append((i, segs))
        if not band:
            return [[0]*W for _ in range(H)]
        b0, cols = band[0]
        s0 = b0 - 5
        pat_h = 6
        pattern = [[0]*W for _ in range(pat_h)]
        for dr in range(pat_h):
            r = s0 + dr
            if r < 0 or r >= H:
                continue
            if 1 <= dr <= 4:
                for s in cols:
                    for dc in range(5):
                        c = s + dc
                        if 0 <= c < W:
                            v = grid[r][c]
                            if v in (1,2,3):
                                pattern[dr][c] = v
            elif dr == 5:
                for s in cols:
                    for dc in range(5):
                        c = s + dc
                        if 0 <= c < W:
                            pattern[dr][c] = 8
        out = [[0]*W for _ in range(H)]
        k = 0
        while True:
            base = s0 + k*6
            if base >= H:
                break
            for dr in range(pat_h):
                r = base + dr
                if 0 <= r < H:
                    for c in range(W):
                        v = pattern[dr][c]
                        if v:
                            out[r][c] = v
            k += 1
        return out
    else:
        # T3
        s0 = None
        cols = None
        for i in range(H):
            segs = []
            c = 0
            while c < W:
                if grid[i][c] != 0 and (c == 0 or grid[i][c-1] == 0):
                    s = c
                    while c < W and grid[i][c] != 0:
                        c += 1
                    if c - s >= 4:
                        segs.append(s)
                else:
                    c += 1
            if len(segs) >= 2:
                s0 = i
                cols = segs
                break
        if s0 is None:
            return [[0]*W for _ in range(H)]
        pat_h = 6
        pattern = [[0]*W for _ in range(pat_h)]
        for dr in range(4):
            r = s0 + dr
            if r < 0 or r >= H:
                continue
            for s in cols:
                for dc in range(4):
                    c = s + dc
                    if 0 <= c < W:
                        v = grid[r][c]
                        if v in (1,2,3):
                            pattern[dr][c] = v
        out = [[0]*W for _ in range(H)]
        k = 0
        while True:
            base = s0 + k*6
            if base >= H:
                break
            for dr in range(4):
                r = base + dr
                if 0 <= r < H:
                    for c in range(W):
                        v = pattern[dr][c]
                        if v:
                            out[r][c] = v
            k += 1
        return out